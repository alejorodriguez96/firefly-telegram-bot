import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext
from telegram import Update

from handlers.commons import init_handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


def default(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


if __name__ == "__main__":
    load_dotenv()
    # Updater
    updater = Updater(token=os.getenv("TOKEN"), use_context=True)
    dispatcher = updater.dispatcher

    # Handlers
    init_handlers(dispatcher)

    # Strat bot
    updater.start_polling()
