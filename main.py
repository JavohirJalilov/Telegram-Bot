from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters


def hello(update,context):
    update.message.reply_text('Welcome to echo bot')
    

def text(update,context):
    text = update.message.text
    update.message.reply_text(text)


updater = Updater('1433923707:AAE32RQiYlMSeeHGJvKMKW4dHqVXaup8rnc')

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text,text))

updater.start_polling()
updater.idle()