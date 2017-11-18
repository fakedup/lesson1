from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import gmtime, strftime
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log')

def main():
    updater = Updater('477291449:AAEh4LG9BVNLGaG5u3WOL_T8DnwsqUxP8_8')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("time", get_time))
    dp.add_handler(MessageHandler(Filters.text, talk_with_user))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Start called'
    logging.info('User command: start')
    update.message.reply_text(text)

def get_time(bot, update):
    text = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    logging.info('User command: time')
    update.message.reply_text(text)

def talk_with_user(bot,update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

main()