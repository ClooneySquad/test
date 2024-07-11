import telebot
from telebot import types

bot = telebot.TeleBot("7358013319:AAFae4MKwf2dryKTiG9CmHybBHmAofjd_UY")

def generate_markup(buttons):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(*(types.KeyboardButton(btn_text) for btn_text in buttons))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Я Ваш бот - рекрутёр. Моя задача - помощь желающим попасть в ряды отряда 'Клуни',для дальнейшего прохождения службы в зоне СВО. Выберите, чем я могу Вам помочь?")
    photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
    bot.send_photo(message.chat.id, photo_url)
    markup = generate_markup(['Про отряд', 'Вакансии', 'Контакты'])
    bot.send_message(message.chat.id, "Выберите одну из следующих опций:", reply_markup=markup)

callback_texts = {
    "Про отряд": "",
    "Вакансии": "Текст для 'Вакансии'",
    "Контакты": "ений",
    "Оператор БпЛА": "онтакты.",
    "Водитель": "товарищ",
    "Штурмовик": "земля",
    "Вернуться в главное меню": "Текст для 'Вернуться в главное меню'"
}

callback_images = {
    "Оператор БпЛА": "https://github.com/ClooneySquad/test/blob/main/drone_pilot.jpg?raw=true",
    "Водитель": "https://github.com/ClooneySquad/test/blob/main/driver.jpg?raw=true",
    "Штурмовик": "https://github.com/ClooneySquad/test/blob/main/asshole.jpg?raw=true"
}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Вакансии":
        markup = generate_markup(['Оператор БпЛА', 'Водитель', 'Штурмовик', 'Назад'])
        bot.send_message(message.chat.id, "Выберите вакансию:", reply_markup=markup)
    elif message.text in ["Оператор БпЛА", "Водитель", "Штурмовик"]:
        photo_url = callback_images[message.text]
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, callback_texts[message.text])
    elif message.text == "Назад":
        markup = generate_markup(['Про отряд', 'Вакансии', 'Контакты'])
        bot.send_message(message.chat.id, "Выберите одну из следующих опций:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, callback_texts.get(message.text, "Извините, я не понял ваш запрос."))

bot.polling()
