import os
import telebot

API_KEY = "5393668969:AAF4K7yPWA9_F3D0ibYgApSN0aFwdfj-8aw"

@bot.messege_handler(commands=['nice'])
def noice(messege):
    bot.reply_to(messege,"congrats")
