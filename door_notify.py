#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import telebot
import time
import requests 
import datetime


# Даты ЗП и аванса
PAID_DATE = 12
PREPAID_DATE = 27

# Настройка бота
chat_id = 111111111                        #замените на свой id
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #замените на TOKEN бота
bot = telebot.TeleBot(TOKEN)

# Быбор системы нумирации пинов (как в кратинке)
GPIO.setmode(GPIO.BCM)
# Настройка пина на вход 
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Имя файла в котором хранится дата последнего увольнения
dimissal_file_name = "last_dismissal_date.txt"

# Текущая дата
today = time.gmtime().tm_mday
# print("Время: ", datetime.now())
door_was_opened = False
was_friday_message = False


def main():
    checkInternet() # Проверяем подключение к интернету
    global door_was_opened
    global today
    global was_friday_message
    # Основной цикл бота
    while True:
        currnet_time = time.gmtime()
        # Если сегодня дверь уже открывали, то просыпаемся раз в 30 мин
        if (door_was_opened):
            checkFriday()
            time.sleep(30 * 60)
        # Сбрасываем флаг если наступил новый день
        if (currnet_time.tm_mday != today):
            today = time.gmtime().tm_mday
            door_was_opened = False
            was_friday_message = False
        # Сигнал с гиркона
        if GPIO.input(4):
            if door_was_opened == False:
                days_str = daysFfterDismissal()
                message = "Дверь открыта"
                if days_str != "-1":
                    message += "\nДней без увольнений - " + days_str
                if checkMoney(currnet_time) != "":
                    message += checkMoney(currnet_time)
                # Отправляем сообщение, поднимаем флаг
                bot.send_message(chat_id, message)
                door_was_opened = True
        time.sleep(1)

# Поступают ли гроши на наши карты сегодня
def checkMoney(time):
    # Если сегодня ЗП
    if time.tm_mday == PAID_DATE:
        return "\nСегодня получим большую копейку"
    # Если сегодня аванс
    if time.tm_mday == PREPAID_DATE:
        return "\nСегодня получим копейку"
    # Если сегодня пятница, а ЗП на выходных
    if (time.tm_wday == 4 and  
        (time.tm_mday + 1 == PAID_DATE or
         time.tm_mday + 2 == PAID_DATE)):
        return "\nСегодня получим большую копейку"
    # Если сегодня пятница, а аванс на выходных
    if (time.tm_wday == 4 and  
        (time.tm_mday + 1 == PREPAID_DATE or
         time.tm_mday + 2 == PREPAID_DATE)):
        return "\nСегодня получим копейку"
    return ""

# Пятничные уведомления
def checkFriday():
    now = datetime.datetime.now()
    today_3_pm = now.replace(hour=15, minute=0, second=0, microsecond=0)
    global was_friday_message
    # Если сегодня пятница после 15 часов
    if (time.gmtime().tm_wday == 4 and
        now > today_3_pm and
        was_friday_message == False):
        bot.send_message(chat_id, 'Не забываем полить цветы и заполнить ПЛМ)')
        was_friday_message = True

# Проверить интернет соединение
def checkInternet():
    internet = False
    while not internet:
        try:
            requests.head("http://www.google.com/", timeout=1)
            # print("The internet connection is active")
            internet = True
        except requests.ConnectionError:
            time.sleep(2)
            pass
            # print("The internet connection is down")

# Количество дней с момента прошлого увольнения
def daysFfterDismissal():
    file = open(dimissal_file_name, "r")
    line = file.readline().split()
    file.close()
    if (len(line) == 0):
        return "-1"
    format = "%Y-%m-%d"
    read_day = datetime.datetime.strptime(line[0], format).date()
    cur_day = datetime.date.today()
    dif = (cur_day - read_day).days 
    return str(dif)
    

main()