from config import urls
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .user import get_subs

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu[0]


def build_reply_markup(chat_id):
    url_list = []
    subs_list = get_subs(chat_id)
    for index, url in enumerate(urls):
        signal = '☒' if str(index) in subs_list else '☐'
        url_list.append(InlineKeyboardButton(
            url['name'] + ' ' + signal, callback_data='subs/{}'.format(index)))
    return InlineKeyboardMarkup(build_menu(url_list, n_cols=2))