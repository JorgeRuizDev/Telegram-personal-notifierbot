from time import sleep

from pyrogram import Client, MessageHandler
from util.util import contains_keywords, notify_user
def main():
    app = Client("init")

    def handler_parms(client, message):
        """
        This function listens for every new message

            If the message comes from your BOT DISPLAY NAME (not the bot name that ends with 'bot'),
            bot does not read the message (as it can create an infinite message loop)
        """
        print(message)
        print(message["chat"]["first_name"])

        if message["chat"]["first_name"] == "Notify":
            return
        if contains_keywords(message["text"]):
            notify_user(message["text"])


    """
    Pyrogram init functions:
    (https://github.com/pyrogram/pyrogram)
    """
    my_handler = MessageHandler(handler_parms)

    app.add_handler(my_handler)

    app.run()


if __name__ == '__main__':
    main()
