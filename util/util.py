from importlib import reload
from telegram.ext import Updater

bot_token = ""

#Keywords is a plain Python List.
from . import keywords

def contains_keywords(message_text: str) -> bool:
    """
    Function that analyzes if a keyword in kewords str list is a
    substring of telegram message

    :param message_text: Telegram recieved text message
    :type message_text: String
    :return: Boolean
    :rtype: Boolean
    """
    reload(keywords)
    for word in keywords.kwords:
        contains = True
        for split_word in word.replace(" ", "").split("AND"):
            if not split_word.lower() in message_text.lower():
                contains = False
        if contains:
            return True
    return False


def notify_user(message_text: str):
    """
    Function that sends to the user a message with a custom string.

    NOTE: This function requires the BOT TOKEN ( https://core.telegram.org/bots/api )

    AND

    Your chat-id with the BOT ( https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id )

    :param message_text: String with the message to be send to the user.
    :type message_text: string
    :return: None
    :rtype: None
    """
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    updater.bot.send_message(chat_id=162610945, text=f"Se ha encontrado una conicidencia!\n\n\n{message_text}")