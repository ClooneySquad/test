import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn = telebot.types.KeyboardButton('Поздароваться')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Поздароваться':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)

bot.polling()
