#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests 
import time
import datetime



def main():
    checkInternet()
    afterLastDismissal()


# Проверить интернет соединение
def checkInternet():
    internet = False
    while not internet:
        try:
            requests.head("http://www.google.com/", timeout=1)
            print('The internet connection is active')
            internet = True
        except requests.ConnectionError:
            pass
            print("The internet connection is down")


def afterLastDismissal():
    file = open('days_after_last_dimissal.txt', 'r')

    s = (file.readline().split())
    # if (len(s) > 0):
    #     cur = int(s[0])
    # else:
    #     cur = -2
    format = "%Y-%m-%d"
    print(s)
    read_data = ""
    datetime.strptime.strptime(read_data, format)
    # file = open('days_after_last_dimissal.txt', 'w')
    # cur += 1
    file.close()
    file = open('days_after_last_dimissal.txt', 'w')

    timenow = datetime.date.today()
    dif = timenow - read_data
    print('dif=', dif)
    print(timenow)
    # file.write(str(cur))
    file.write(str(timenow))
    file.close()


main()


# checkInternet()