from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
echo_handler = MessageHandler(Filters.text, echo)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def start(bot, update):
    update.message.reply_text(u'欢饮欢迎')

def weather(bot, update):
    update.message.reply_text(u'欢饮欢迎')



updater = Updater('318248420:AAHgJyTmE7FUJQdxbGnd2ERoDdg6IVfjyy4')
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
