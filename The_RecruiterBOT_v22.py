import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo_url = 'https://github.com/ClooneySquad/test/blob/main/photo_clooney.jpg?raw=true'
    bot.send_photo(message.chat.id, photo_url)
    bot.send_message(message.chat.id, "Привет! Я отправил тебе изображение.")

bot.polling()
