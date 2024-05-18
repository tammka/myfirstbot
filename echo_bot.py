import telebot
bot = telebot.TeleBot('6418123443:AAHbnndKgUvCjy7l8exqNV8NsgMaY_TPymw')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

#bot.polling(none_stop=True, interval=0)
