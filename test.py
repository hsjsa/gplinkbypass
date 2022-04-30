import os
import telebot
from telegram.ext import CommandHandler, run_async

API_KEY = "5393668969:AAF4K7yPWA9_F3D0ibYgApSN0aFwdfj-8aw"

@run_async
def noice(update, context):
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        link = args[1]
sendMessage(link, context.bot, update)
