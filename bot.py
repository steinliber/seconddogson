# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chat import deepThought
from os import listdir
from os.path import isfile, join
import logging
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def echo(bot, update):
    return_msg = str(deepThought.get_response(update.message.text))
    if return_msg == '全然不懂你在说什么':
        catfiles = [f for f in listdir('static/cat') if isfile(join('static/cat', f))]
        picture = random.choice(catfiles)
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(picture, 'rb'))
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
