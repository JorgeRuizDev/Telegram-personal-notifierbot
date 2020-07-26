# Telegram-personal-notifierbot

This python bot notifies you when you receive a message that contains ONE or MORE specific KEYWORDS.

It also allows you to modify the keywords remotely.

## Dependencies:

### **Pyrogram:**
[Github Repository](https://github.com/pyrogram/pyrogram)
	
    $ pip install pyrogram
  or

    $ pip3 install pyrogram

### **python-telegram-bot**
[Github repository](https://github.com/python-telegram-bot/python-telegram-bot)

    $ pip install python-telegram-bot --upgrade
  or

    $ pip3 install python-telegram-bot --upgrade

## How to install

    $ git clone https://github.com/JorgeRuizDev/Telegram-personal-notifierbot
    $ cd Telegram-personal-notifierbot
    
## How to configure
### Prerequisites

A  [Telegram BOT](https://core.telegram.org/bots)  and a [Telegram Developer Account](https://my.telegram.org/apps)

    The Telegram BOT should generate:
	    BOT TOKEN
	    BOT NAME (not the one that ends with _bot)
	    
    The Telegram Developer Account should have
	    App api_id
	    App api_hash

### This bot has 4 .py files

    bot.py ->  Main Telegram bot. Has the message handler for the Bot Commands 
		       This specifi bot has the /cholos command that allows the modification
		       of keywords.py remotely.
	
	main.py -> Main chat fetcher. For every new your account receives, 
			   this script will search for any substring of Keywords.py
	
	folder ./util/	
	util.py -> Contains the functions to send a personal message through the BOT and
		       search for substrings of keywords.py

	keywords.py -> contains a python String list (kwords) that stores the main words 

### Add your **ACCOUNT**  and BOT

    As this bot uses PYROGRAM for managing NEW messages and python-telegram-bot for 
    sending and processing the BOT messages, we invite you to read both libraries
    "Getting Started" documentation.


#### Pyrogram
Pyrogram creates a **config.ini** file in the root of the project. You need to include your 	
**App api_id** and **App api_hash** in order to successfully fetch new messages.
For security reasons, the first login will require a  two step authentication with your mobile phone 
(same as login to Telegram in a secondary device)

#### python-telegram-bot
Python-Telegram-Bot library is used in **TWO** scripts.

 - **bot.py** if you want to edit **/util/keywords.py** via telegram
 - **util/util.py** if you want to get a Telegram Notification if a message 
		 contains a **/util/keywords.py** substring.
		 
In both scripts there is a variable that stores the BOT TOKEN (obtained via [Telegram's Bot Father](https://t.me/botfather))
Just update that variable with the bot token

    bot_token = "YOUR STRING TOKEN"

### Bot Security
All bots are **PUBLIC**, if you don't want anybody to use ANY of the BOTS commands, you need to specify
the users that are allowed to do so. 

In this case, **bot.py** has a variable that specifies the ONLY user that can use **/start** and
 **/create** commands.
  

    admin_username = "@username"

### Receiving Messages from the BOT
All bots are **PUBLIC**, so Telegram's BOT API requires the USER and the BOT to use an individual **CHATID**.
This **CHAT ID** is UNIQUE, and is established for the first time when the user starts a conversation with the bot.

If you want to receive messages from the BOT, you need your chat ID. There is no automatic chat id feature, so the user needs to implement it manually

#### [HOW TO OBTAIN YOUR CHAT ID](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)

Find the following line and update **chat_id=** with your ID.

    updater.bot.send_message(chat_id=, text=f"Se ha encontrado una conicidencia!\n\n\n{message_text}")

### Avoid INFINITE NOTIFICATIONS LOOPING
If you are notifying yourself with a copy of the message, the **MESSAGE FETCHER will find the substring in the copy of the message**. And throw a new notification. 

This will create an **INFINITE LOOP**

To avoid this, main.py contains a line which skips the messages received from the bot

**first_name** is the name of the BOT that is DISPLAYED on top of the chat, not the bot ID that usually ends with **"_bot"**

    if message["chat"]["first_name"] == "Notify":

![enter image description here](https://i.imgur.com/M40kadb.png)

