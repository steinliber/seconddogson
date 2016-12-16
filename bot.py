# -*- coding: utf-8 -*-
import logging
import random
from os import listdir
from os.path import isfile, join

from chat import deepThought
from settings import BOT_TOKEN
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from weather import WeatherAPI

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def echo(bot, update):
    return_msg = str(deepThought.get_response(update.message.text))
    if return_msg == '全然不懂你在说什么':
        catfiles = [join('static/cat', f) for f in listdir('static/cat')]
        picture = random.choice(catfiles)
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(picture, 'rb'))
    bot.sendMessage(chat_id=update.message.chat_id, text=return_msg)


def start(bot, update):
    update.message.reply_text(u'欢饮欢迎')

def weather(bot, update):
    weather_api = WeatherAPI()
    weather_text = weather_api.get_weather()
    bot.sendMessage(chat_id=update.message.chat_id, text=weather_text)
    suggest_text = weather_api.get_suggestion()
    bot.sendMessage(chat_id=update.message.chat_id, text=suggest_text)


echo_handler = MessageHandler(Filters.text, echo)

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
