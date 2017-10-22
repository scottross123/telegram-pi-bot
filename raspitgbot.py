from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ForceReply
from tokens import raspi_b
from ety import find_ety


def start(bot, update):
    update.message.reply_text('Hello! I\'m the telegram bot running on Scott\'s RaspberryPi! \n  \n Here\'s a list of my commands: \n \n /test \n /echo')


def test(bot, update):
    update.message.reply_text('this is a test')


# def echo(bot, update):
#     update.message.reply_text(update.message.text)


def etymology(bot, update):
    #bot.send_message(chat_id=update.message.chat_id, text="What word would you like to find the etymology of?")
    #f_ety = find_ety(update.message.text)
    print(find_ety(update.message.text))
    #update.message.reply_text(find_ety('hello'))


def main():

    updater = Updater(token=raspi_b)
    dispatcher = updater.dispatcher

    # /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # /test command
    test_handler = CommandHandler('test', test)
    dispatcher.add_handler(test_handler)

    # /echo command
    # echo_handler = MessageHandler(Filters.text, echo)
    # dispatcher.add_handler(echo_handler)

    # /etymology command
    ety_handler = MessageHandler(Filters.text, etymology)
    dispatcher.add_handler(ety_handler)
    #
    # convo_handler = ConversationHandler(
    #     entry_points=[ety_handler],
    #
    #     states={
    #         WORD: [MessageHandler(Filters.text, text),
    #                 CommandHandler('find', find_etymology)]
    #     }
    # )
    # dispatcher.add_handler(conv_handler)

    updater.start_polling()
    print('working')


if __name__ == '__main__':
    main()
