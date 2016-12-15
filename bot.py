from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    print('sss')
    update.message.reply_text(u'欢饮欢迎')

def weather(bot, update):
    print('xxx')
    update.message.reply_text(u'欢饮欢迎')

updater = Updater('318248420:AAHgJyTmE7FUJQdxbGnd2ERoDdg6IVfjyy4')

updater.dispatcher.add_handler(CommandHandler('weather', weather))

updater.start_polling()
updater.idle()
