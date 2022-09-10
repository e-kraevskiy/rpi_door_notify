#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests 
import time
import datetime



def main():
    # checkInternet()
    ans = afterLastDismissal()
    print("res=",ans)


# Проверить интернет соединение
def checkInternet():
    internet = False
    while not internet:
        try:
            requests.head("http://www.google.com/", timeout=1)
            print("The internet connection is active")
            internet = True
        except requests.ConnectionError:
            pass
            print("The internet connection is down")


def afterLastDismissal():
    file = open("days_after_last_dimissal.txt", "r")

    s = file.readline().split()
    if (len(s) == 0):
        return -1
    format = "%Y-%m-%d"
    print(s)
    read_data = ""
    read_day = datetime.datetime.strptime(s[0], format).date()
    print("read_day=", read_day)
    # cur += 1
    file.close()


    # file = open('days_after_last_dimissal.txt', 'w')
    cur_day = datetime.date.today()
    dif = (cur_day - read_day).days 
    return dif
    # print(timenow)
    # file.write(str(cur))
    # file.write(str(timenow))
    # file.close()


main()
