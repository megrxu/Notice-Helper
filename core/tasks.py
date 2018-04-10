from .parser import render_article
from config import urls
from telegram import ParseMode
from .article import get_articles
from .user import get_users


def refresh_task(bot, job):
    users = get_users()

    def send(article, feed_index):
        text = render_article(article, feed_index)
        for user in users:
            if str(feed_index) in user[1]:
                bot.send_message(chat_id=user[0],
                                 text=text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

    # def test(article, feed):
    #     print(article.published)
    get_articles(urls, send)
