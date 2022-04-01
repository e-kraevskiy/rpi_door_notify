#!/usr/bin/env python3

import time
import keyboard


currnet_day = time.gmtime().tm_mday
print('Сегодня', currnet_day, 'число')
current_time = time.gmtime()
print('Сегодня', current_time.tm_mday, 'число')
