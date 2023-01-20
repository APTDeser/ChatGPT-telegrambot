import asyncio
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from easychatgpt import ChatClient

OPENAI_EMAIL = os.getenv("OPENAI_EMAIL")
OPENAI_PASSWORD = os.getenv("OPENAI_PASSWORD")

chatgpt = ChatClient("OPENAI_EMAIL","OPENAI_PASSWORD",headless=False)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    reply = chatgpt.interact(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

updater = Updater(token="YOURTOKEN", use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()