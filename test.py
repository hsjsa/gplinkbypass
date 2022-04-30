import os
import telebot
from telegram.message import Message
from telegram.update import Update
import time
from telegram.error import TimedOut, BadRequest
from telegram.ext import CommandHandler, run_async

API_KEY = "5393668969:AAF4K7yPWA9_F3D0ibYgApSN0aFwdfj-8aw"

def sendMessage(text: str, bot, update: Update):
    try:
        return bot.send_message(update.message.chat_id,
                            reply_to_message_id=update.message.message_id,
                            text=text, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))

@run_async
def noice(update, context):
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        url = args[1]
sendMessage({url}, context.bot, update)
