from telegram.ext import Updater, CommandHandler, Filters
from util.keywords import kwords

#Var that stores the string with the only user that the bot CAN interact
admin_username = "@jorgestar29"
bot_token = ""

def start(update, context):
    # /start command

    """Send a message when the command /start is issued."""
    update.message.reply_text('Cargando Bot!')
    update.message.reply_text('Comandos:\n'
                              '/chollos <tipo> <argumentos>\n'
                              'Ejemoplo: /chollos help\n')
    print(context)

def chollos(update, context):

    # /chollos command

    tipo: str = context.args[0]

    if tipo == 'help':
        chollos_help(update)
    if tipo == 'show':
        chollos_show(update)
    if tipo == 'remove':
        chollos_remove(update, int(context.args[1]))
        update_keywords(kwords)
    if tipo == 'add':
        chollos_add(update, context.args)
        update_keywords(kwords)


def chollos_add(update, raw_args: str):
    """
    This function adds a new element to the Keywords list.
    From the args of the command (/command <args>) it removes the FIRST word
    as it is the control keyword (add / remove / help...)

    :return: None, but sends the user a message
    :rtype: None
    """
    args = ""
    for word in raw_args:
        if word != "add":
            args += word + " "

    if len(args) <= 0:
        return

    print(args)
    kwords.append(args)
    update.message.reply_text(f"{args} ha sido añadido satisfactoriamente")


def chollos_help(update):
    """
    Help function
    :param update:
    :type update:
    :return:
    :rtype:
    """
    update.message.reply_text('Use el comando /chollos <tipo> <argumento>\n\n'
                              'Hay 4 tipos disponibles: help, add, show y remove.\n\n'
                              '/chollos add Echo AND Alexa -> Añade a la lista de avisos que todos los mensajes que contengan las palabras Alexa y Echo sean notificados.\n\n'
                              '/chollos show -> Muestra todos los filtros numerados.\n\n'
                              '/chollos remove <num_chollo> -> Elimina del listado el chollo correspondiente al SHOW actual.\n\n')


def update_keywords(keywords):
    """
    This funcion stores into the util/keywords.py file the keywords array.
    :param keywords: KeyWords to be stored
    :type keywords: string list
    :return: None
    :rtype: None
    """
    f = open("util/keywords.py", mode="w")
    f.write(f"kwords = {keywords}")
    f.close()


def chollos_remove(update, chollo: int):
    """
    This function removes a keyword from the keywords list via it's index
    :param update: Update object to reply the user
    :param chollo: index of the intem to be deleted
    :type chollo: int
    :return: sends a message
    :rtype: None
    """
    chollo = int(chollo)
    print(len(kwords))
    if chollo >= len(kwords) or chollo < 1:
        update.message.reply_text("Argumento inválido")
        return
    chollo = chollo - 1
    chollo_name = kwords[chollo]

    del kwords[chollo]

    update.message.reply_text(f"{chollo_name} ha sido eliminado.")


def chollos_show(update):
    """
    Displays the user the Keywords list as a Telegram Message
    """
    listado: str = ""
    i: int = 1
    for word in kwords:
        listado += f"{i}: {word}\n"
        i = i + 1

    update.message.reply_text(listado)


def main():


    #Token = Bot Token (https://core.telegram.org/bots/api)
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    #Handler of /start command
    dispatcher.add_handler(CommandHandler("start", start, Filters.user(username=admin_username)))

    #Handler of /chollos command
    dispatcher.add_handler(CommandHandler("chollos", chollos, pass_args=True, filters=Filters.user(username=admin_username)))
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
