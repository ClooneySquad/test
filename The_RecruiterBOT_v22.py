import telebot

bot = telebot.TeleBot('7358013319:AAFae4MKwf2dryKTiG9CmHybBHmAofjd_UY')

def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Текст 1')
    itembtn2 = telebot.types.KeyboardButton('Текст 2')
    itembtn3 = telebot.types.KeyboardButton('Вакансии')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Привет, {}! Это приветственный текст".format(message.from_user.first_name), reply_markup=markup)
    photo_url = 'https://github.com/ClooneySquad/test/blob/main/test3.jpg?raw=true'
    bot.send_photo(message.chat.id, photo_url)

def vacancies_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Вакансия 1')
    itembtn2 = telebot.types.KeyboardButton('Вакансия 2')
    itembtn3 = telebot.types.KeyboardButton('Вакансия 3')
    itembtn4 = telebot.types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выбери вакансию или вернись назад:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    main_menu(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Текст 1':
        bot.send_message(message.chat.id, "Это первый текст")
    elif message.text == 'Текст 2':
        bot.send_message(message.chat.id, "Это второй текст")
    elif message.text == 'Вакансии':
        vacancies_menu(message)
    elif message.text == 'Вакансия 1':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/test3.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, "Текст для Вакансии 1")
    elif message.text == 'Вакансия 2':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/testtesttest.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, "Текст для Вакансии 2")
    elif message.text == 'Вакансия 3':
        photo_url = 'https://github.com/ClooneySquad/test/blob/main/test2.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, "Текст для Вакансии 3")
    elif message.text == 'Назад':
        main_menu(message)

bot.polling()
