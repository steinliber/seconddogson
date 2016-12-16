# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chat import deepThought
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def echo(bot, update):
    return_msg = str(deepThought.get_response(update.message.text))
    if return_msg == 'NO!':
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open('static/cat.jpg', 'rb'))
    bot.sendMessage(chat_id=update.message.chat_id, text=return_msg)


def start(bot, update):
    update.message.reply_text(u'欢饮欢迎')

def weather(bot, update):
    update.message.reply_text(u'欢饮欢迎')


echo_handler = MessageHandler(Filters.text, echo)

updater = Updater('318248420:AAHgJyTmE7FUJQdxbGnd2ERoDdg6IVfjyy4')
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
