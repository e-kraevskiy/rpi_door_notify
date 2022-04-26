#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import telepot
import time

from datetime import datetime

# Даты ЗП и аванса
PAID_DATE = 12
PREPAID_DATE = 27

# Настройка бота
chat_id = 111111111111                        #замените на свой id
# TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #замените на TOKEN бота
bot = telepot.Bot(TOKEN)

# Быбор системы нумирации пинов (как в кратинке)
GPIO.setmode(GPIO.BCM)
# Настройка пина на вход 
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Текущая дата
today = time.gmtime().tm_mday
print("Время: ", datetime.now())
door_was_opened = False
was_friday_message = False

# Поступают ли гроши на наши карты сегодня
def checkMoney(time):
    # Если сегодня ЗП
    if time.tm_mday == PAID_DATE:
        bot.sendMessage(chat_id, 'Дверь открыта\nСегодня получим большую копейку')
        return True
    # Если сегодня аванс
    if time.tm_mday == PREPAID_DATE:
        bot.sendMessage(chat_id, 'Дверь открыта\nСегодня получим копейку')
        return True
    # Если сегодня пятница, а ЗП на выходных
    if (time.tm_wday == 4 and  
        (time.tm_mday + 1 == PAID_DATE or
         time.tm_mday + 2 == PAID_DATE)):
        bot.sendMessage(chat_id, 'Дверь открыта\nСегодня получим большую копейку')
        return True
    # Если сегодня пятница, а аванс на выходных
    if (time.tm_wday == 4 and  
        (time.tm_mday + 1 == PREPAID_DATE or
         time.tm_mday + 2 == PREPAID_DATE)):
        bot.sendMessage(chat_id, 'Дверь открыта\nСегодня получим копейку')
        return True
    return False

# Пятничные уведомления
def checkFriday():
    now = datetime.now()
    today_3_pm = now.replace(hour=15, minute=0, second=0, microsecond=0)
    global was_friday_message
    # Если сегодня пятница после 15 часов
    if (time.gmtime().tm_wday == 4 and
        now > today_3_pm and
        was_friday_message == False):
        bot.sendMessage(chat_id, 'Не забываем полить цветы и заполнить ПЛМ)')
        was_friday_message = True

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
    if GPIO.input(4):
        if door_was_opened == False:
            if checkMoney(currnet_time) == False:
                bot.sendMessage(chat_id, 'Дверь открыта')
            door_was_opened = True
    time.sleep(1)