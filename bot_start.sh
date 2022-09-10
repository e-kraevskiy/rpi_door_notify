#!/bin/bash

sleep 10
sudo python /home/pi/door_notify.py &
sudo python /home/pi/message_handler.py &
