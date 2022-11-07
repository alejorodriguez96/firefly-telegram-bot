import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext
from telegram import Update
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    load_dotenv()
    # Updater
    updater = Updater(token=os.getenv('TOKEN'), use_context=True)
    dispatcher = updater.dispatcher
    
    # Handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    # Strat bot
    updater.start_polling()
