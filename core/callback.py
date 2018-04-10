from .utils import build_reply_markup
from .user import get_subs, del_subs, add_subs

def callback_dispatcher(bot, update):
    call_str = update.callback_query['data'].split('/')
    chat_id = update.callback_query['message']['chat']['id']
    message_id = update.callback_query['message']['message_id']
    if call_str[0] == 'subs':
        subs = get_subs(chat_id)
        if call_str[1] in subs:
            del_subs(chat_id, call_str[1])
        else:
            add_subs(chat_id, call_str[1])
        bot.answer_callback_query(
            callback_query_id=update.callback_query.id, text='订阅更新生效。')
        reply_markup = build_reply_markup(chat_id)
        bot.edit_message_text(
            chat_id=chat_id, message_id=message_id, text='你的订阅：', reply_markup=reply_markup)
    else:
        bot.answer_callback_query(
            callback_query_id = update.callback_query.id, text='输入不合法')
