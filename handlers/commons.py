from telegram.ext import CallbackContext, CommandHandler, Dispatcher
from telegram.ext import MessageHandler, Filters
from telegram import Update


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


def default(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


def init_handlers(dispatcher: Dispatcher):
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    default_handler = MessageHandler(Filters.all, default)
    dispatcher.add_handler(default_handler)
