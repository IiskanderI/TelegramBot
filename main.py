from telegram.ext import *

count = 0


def sms(bot, update):
    global count
    count += 1
    print(f'{count} times people pressed /start!')
    bot.message.reply_text('Hello and welcome traveller to the wild lands!')


def main():
    my_bot = Updater('5726825159:AAEH8as7sMean-99KhaF0gpUgX5EF2XjiVs', use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.start_polling()
    my_bot.idle()


main()
