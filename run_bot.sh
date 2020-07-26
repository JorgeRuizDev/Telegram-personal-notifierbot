#!/bin/bash
cd /home/pi/bots/telegram_notify_bot/source/
/usr/bin/python3  main.py &
/usr/bin/python3  bot.py &
