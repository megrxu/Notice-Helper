from telegram.ext import Updater, CommandHandler
from telegram import ChatAction, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from .article import get_articles
from .parser import render_article
from config import urls
from .utils import build_menu, build_reply_markup
from .user import add_user, if_new_user


def hello(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

# def refresh(bot, update):
#     def send(article, feed):
#         text = render_article(article, feed)
#         bot.send_message(chat_id=update.message.chat_id,
#                          text=text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
#     get_articles(urls, send)


def start(bot, update):
    chat_id = update.message.chat_id
    if if_new_user(chat_id):
        add_user(chat_id, '')
    reply_markup = build_reply_markup(chat_id)
    bot.send_message(chat_id=chat_id, text='你的订阅：',
                     reply_markup=reply_markup)
