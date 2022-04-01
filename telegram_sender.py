#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import telepot

text = sys.argv[1]
chat_id = 308056206  #замените на свой id
TOKEN = "5079941131:AAHOqcD2QzEPjYNDRUY21yPuJPZMItvmH-Y"
bot = telepot.Bot(TOKEN)
bot.sendMessage(chat_id, str(text))
