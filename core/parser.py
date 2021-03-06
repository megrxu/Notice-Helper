import feedparser
from bs4.dammit import EncodingDetector
from bs4 import BeautifulSoup
from .article import Article
from datetime import datetime
import requests


def parse_rss(url, feed):
    d = feedparser.parse(url)
    return d.entries


def parse_html(url):
    try:
        resp = requests.get(url)
        resp.encoding = 'gb2312'
    except:
        return None
    http_encoding = resp.encoding if 'charset' in resp.headers.get(
        'content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(
        resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    return BeautifulSoup(resp.text, 'html.parser')


def parse_college(url, feed):
    soup = parse_html(url)
    if soup == None:
        return []
    articles = []
    for ul in soup.find_all('ul', attrs={'class': 'cg-news-list'}):
        for li in ul.find_all('li'):
            try:
                text = li.find('span', attrs={'class': 'art-date'}).text
            except:
                continue 
            date = parse_date(text)
            try:
                title = li.a['title']
                true_url = url + li.a['href']
            except:
                continue
            articles.append(
                Article(title, feed, date, true_url))
    return articles


def parse_cspo(url, feed):
    soup = parse_html(url)
    if soup == None:
        return []
    articles = []
    title, date, link = '', '', ''
    for index, item in enumerate(soup.find_all('td', attrs={'class': 'header-yz jishigx-s'})):
        if index % 2 == 1:
            date = parse_date(item.text)
            articles.append(
                Article(title, feed, date, link))
        else:
            title = item.find_all('a')[-1].text
            link = url + item.find_all('a')[-1]['href']
    return articles

def parse_cse(url, feed):
    soup = parse_html(url)
    if soup == None:
        return []
    url = 'http://www.cse.zju.edu.cn/'
    articles = []
    title, date, link = '', '', ''
    div = soup.find('div', attrs={'id': 'main0'})
    for item in(div.find_all('ul')):
        for li in item.find_all('li'):
            if li.span:
                date = parse_date(li.span.text)
                link = url + li.a['href']
                title = li.a['title']
                articles.append(
                    Article(title, feed, date, link))
    return articles


def parse_date(text):
    if not('201' in text):
        if('[' in text):
            datetime_object = datetime.strptime(text, '[%m-%d]')
            year = datetime.today().year if datetime.today(
            ).month >= datetime_object.month else datetime.today().year - 1
            datetime_object = datetime_object.replace(year=year)
        elif (']' in text):
            return parse_date('[' + text)
        else:
            datetime_object = datetime.strptime(text, '%m-%d')
            year = datetime.today().year if datetime.today(
            ).month >= datetime_object.month else datetime.today().year - 1
            datetime_object = datetime_object.replace(year=year)
    else:
        if not('[' in text):
            datetime_object = datetime.strptime(text, '%Y-%m-%d')
        else:
            datetime_object = datetime.strptime(text, '[%Y-%m-%d]')
    return datetime_object.strftime("%Y-%m-%d")

def render_article(article, feed):
    text = """
*{title}*
――
{feed} | [Link]({link}) | {date}
""".format(title=article.title, link=article.link, feed=article.feed, date=article.published)
    return text
