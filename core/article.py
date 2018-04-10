import sqlite3


class Article(object):
    def __init__(self, title, feed, published, link, summary=''):
        self.title = title
        self.feed = feed
        self.published = published
        self.link = link
        self.summary = summary


def get_conn():
    conn = sqlite3.connect('data/data.db')
    db = conn.cursor()
    return (conn, db)


def if_new_article(title, date):
    conn, db = get_conn()
    db.execute(
        "SELECT * FROM articles WHERE TITLE = ? AND DATE = ?", (title, date))
    result = db.fetchall()
    conn.close()
    if result:
        return False
    else:
        return True


def add_article(title, date, feed, link):
    conn, db = get_conn()
    db.execute("INSERT INTO articles VALUES (?,?,?,?)",
               (title, date, feed, link))
    conn.commit()
    conn.close()


def get_articles(urls, notify=lambda: None):
    for index, url in enumerate(urls):
        articles, feed_index = url['parser'](url['link'], url['name']), index
        for article in articles:
            title, date, link = article.title, article.published, article.link
            if if_new_article(title, date):
                add_article(title, date, urls[feed_index]['name'], link)
                notify(article, feed_index)

def read_articles(feed, limit=20):
    conn, db=get_conn()
    db.execute("SELECT * FROM articles WHERE feed like ? ORDER BY strftime('%Y-%m-%d', date) DESC LIMIT ?", ("%" + feed + "%", limit,))
    result = db.fetchall()
    conn.close()
    articles = []
    for item in result:
        articles.append(Article(item[0], item[2], item[1], item[3]))
    return articles