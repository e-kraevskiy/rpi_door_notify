#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import time
import datetime

# Настройка бота
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #замените на TOKEN бота
bot = telebot.TeleBot(TOKEN)


# Имя файла в котором хранится дата последнего увольнения
dimissal_file_name = "last_dismissal_date.txt"

# Функция, обрабатывающая команду /dismissal
@bot.message_handler(commands=["dismissal"])
def dismissal_handler(message):
    msg = message.text.split()
    if len(msg) == 1:
        bot.send_message(message.chat.id, "Вы не ввели дату\nПопробуйте снова в формете YYYY-MM-DD")
        return
    msg = msg[1]
    if msg == "false":
        file = open(dimissal_file_name, 'w')
        file.close()
        bot.send_message(message.chat.id, "Уведомления о количестве дней с момента увольнения отключены")
        return

    format = "%Y-%m-%d"
    try:
        read_day = datetime.datetime.strptime(msg, format).date()
    except ValueError:
        bot.send_message(message.chat.id, "Не удалось прочитать дату\nПопробуйте снова в формете YYYY-MM-DD")
        return
    cur_day = datetime.date.today()
    dif = (cur_day - read_day).days
    if dif < 0:
        bot.send_message(message.chat.id, "К сожалению, увольняться в будущем нельзя")    
        return
    bot.send_message(message.chat.id, "Дата успешно установлена\nДней с момента последнего увальнения: " + str(dif))
    file = open(dimissal_file_name, 'w')
    file.write(str(read_day))
    file.close()
    

bot.polling()
