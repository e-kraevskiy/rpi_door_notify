#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# Быбор системы нумирации пинов (как в кратинке)
GPIO.setmode(GPIO.BCM)
# Настройка пина на вход 
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ch4_state = GPIO.input(4)

# Текущая дата
currnet_day = time.gmtime().tm_mday
print('Сегодня', currnet_day, 'число')
door_opened = False


try:
    while True:
    	day = time.gmtime().tm_mday
    	if (currnet_day != day)
    		door_opened = False
        if GPIO.input(4) and not door_opened:
            print('NOTIFICATION')
            door_opened = True
        else:
            print('CLOSED')
        time.sleep(0.1)
except KeyboardInterrupt:
	print('KeyboardInterrupt')
	# Сброс всех какнол по завершению работы 
#    GPIO.cleanup()

