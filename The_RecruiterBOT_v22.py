import telebot

bot = telebot.TeleBot('7358013319:AAFae4MKwf2dryKTiG9CmHybBHmAofjd_UY')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Вакансия 1')
    itembtn2 = telebot.types.KeyboardButton('Вакансия 2')
    itembtn3 = telebot.types.KeyboardButton('Вакансия 3')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Привет! Нажми на одну из кнопок:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Вакансия 1':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
    elif message.text == 'Вакансия 2':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
    elif message.text == 'Вакансия 3':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)

bot.polling()
