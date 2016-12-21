# -*- coding: utf-8 -*-
import logging
import random
from os import listdir
from os.path import isfile, join
import urllib.request

from chat import deepThought
from settings import BOT_TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from weather import WeatherAPI

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def echo(bot, update):
    return_msg = str(deepThought.get_response(update.message.text))
    if return_msg == '全然不懂你在说什么':
        catfiles = [join('static/cat', f) for f in listdir('static/cat')]
        picture = random.choice(catfiles)
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(picture, 'rb'),)
    bot.sendMessage(chat_id=update.message.chat_id, text=return_msg)

def img(bot, update):
    groups = list()
    groups.append(
	       [InlineKeyboardButton(text='私房照', callback_data='personal'), InlineKeyboardButton(text='公共照', callback_data='public')]
    )
    # groups.append(
	#        [InlineKeyboardButton(text='公共照', callback_data='public')]
    # )
    pics = [(x.file_id, x.file_size) for x in update.message.photo]
    max_pics = max(pic[1] for pic in pics)
    file_id = [x for x in pics if x[1] == max_pics][0][0]
    files = bot.get_file(file_id)
    file_name = files['file_path'].split('/')[-1]
    urllib.request.urlretrieve(files['file_path'], join('static', 'saved', file_name))
    bot.sendMessage(chat_id=update.message.chat_id, text='请选择要保存的分类', reply_markup=InlineKeyboardMarkup(groups))

def start(bot, update):
    update.message.reply_text(u'欢饮欢迎')

def weather(bot, update):
    weather_api = WeatherAPI()
    weather_text = weather_api.get_weather()
    bot.sendMessage(chat_id=update.message.chat_id, text=weather_text)
    suggest_text = weather_api.get_suggestion()
    bot.sendMessage(chat_id=update.message.chat_id, text=suggest_text)


echo_handler = MessageHandler(Filters.text, echo)
img_handler = MessageHandler(Filters.photo, img)

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(echo_handler)
updater.dispatcher.add_handler(img_handler)

updater.start_polling()
updater.idle()