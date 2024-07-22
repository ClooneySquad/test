import json
import telebot
import re

bot = telebot.TeleBot('7358013319:AAFae4MKwf2dryKTiG9CmHybBHmAofjd_UY')

MANAGER_ID = ['7093997184', '917086860', '987654321']
USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(list(users), file)

unique_users = load_users()

def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton("Про отряд")
    itembtn2 = telebot.types.KeyboardButton('Контакты')
    itembtn3 = telebot.types.KeyboardButton('Вакансии')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Привет, {}! Я Ваш бот - рекрутёр. Моя задача - помощь желающим попасть в ряды отряда 'Клуни',для дальнейшего прохождения службы в зоне СВО. Выберите, чем я могу Вам помочь?".format(message.from_user.first_name), reply_markup=markup)
    photo_url = 'https://github.com/ClooneySquad/test/blob/1d7155ca09993fca84671531d491ac638e7e27bf/ScriptData/SkriptMedia/MainLogo.jpg?raw=true'
    bot.send_photo(message.chat.id, photo_url)

def vacancies_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Оператор дрона')
    itembtn2 = telebot.types.KeyboardButton('Водитель')
    itembtn3 = telebot.types.KeyboardButton('Штурмовик')
    itembtn4 = telebot.types.KeyboardButton('Назад')
    itembtn5 = telebot.types.KeyboardButton('Медик')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn5, itembtn4)
    bot.send_message(message.chat.id, "Выбери вакансию или вернись назад:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    username = user.username
    if not username or re.search(r'[\U0001F600-\U0001F64F]', username):
        username = "Нестандартное имя, вывести невозможно"
    main_menu(message)
    if user.id not in unique_users:
        unique_users.add(user.id)
        save_users(unique_users)
        usersval = len(unique_users)
        for manager_id in MANAGER_IDS:
            bot.send_message(manager_id, f"Пользователь {username} впервые подключился к боту-рекрутёру. Всего новых пользователей, подключившихся к боту = {usersval}.")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Про отряд':
        bot.send_message(message.chat.id, """Легендарный отряд «КЛУНИ» объявляет набор бойцов для участия в специальной военной операции. Отряд был создан с начала СВО и носит имя своего первого командира с позывным «КЛУНИ», погибшего в марте 2022 г., защищая свою родную землю. В настоящее время подразделение выполняет боевые задачи совместно с Вооруженными Силами Российской Федерации.  

С начала СВО личный состав отряда удостоен следующими государственными наградами: 
1.	Герой ДНР – 1
2.	Орден Мужества – 54
3.	Медаль за Отвагу – 82

Кандидатам на службу предлагается денежное содержание от 220 000 руб. в месяц. Бесплатное питание, полное обеспечение экипировкой высокого качества, СИБЗ (класс защиты 4+).

За результативную работу существует финансовое вознаграждение. Проезд к месту службы оплачивается за счёт отряда (при сохранении проездных билетов и кассовых чеков, подтверждающих оплату). За ранение предусмотрены социальные выплаты до 3-х миллионов руб.

В отряде «КЛУНИ» для специалистов предусмотрены служебные контракты продолжительностью 6 и 12 месяцев. После завершения каждого контракта предусмотрен оплачиваемый отпуск. По окончании 1-го контракта оформляется удостоверение ветерана боевых действий

Кандидатам на службу при себе иметь паспорт, справки или другие подтверждающие документы отсутствия хронических заболеваний, в том числе СПИД, ВИЧ, Гепатит, Туберкулёз. 
На службу также принимаются иностранные граждане. Для иностранцев существует возможность оформить гражданство Российской Федерации.
""")
    elif message.text == 'Контакты':
        bot.send_message(message.chat.id, """По всем вопросам: @ClooneyRecruiter \n+79495660687 (только для сообщений в телеграмм), \nНаша 'Отчетная' группа в телеграмм: https://t.me/ClooneySquad""")
    elif message.text == 'Вакансии':
        vacancies_menu(message)
    elif message.text == 'Оператор дрона':
        photo_url = 'https://github.com/ClooneySquad/test/blob/1d7155ca09993fca84671531d491ac638e7e27bf/ScriptData/SkriptMedia/DronePilot.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, """Отряд «Клуни» приглашает освоить современную и востребованную специальность оператора БпЛА (коммерческие дроны, FPV-дроны, дроны экстра-класса).
Опыт работы (управления дронами) приветствуется. Есть возможность пройти обучение с нуля. 
Если ты готов изучать новые технологии и быть главным оружием современной войны - пиши на номер в разделе "Контакты".
""")
    elif message.text == 'Водитель':
        photo_url = 'https://github.com/ClooneySquad/test/blob/1d7155ca09993fca84671531d491ac638e7e27bf/ScriptData/SkriptMedia/Driver.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, """Отряд «Клуни» приглашает водителей категории «В,С» с опытом вождения, обслуживания и ремонта автомобилей марки «УАЗ» и «КАМАЗ». 
Если ты готов ценить и заботиться о вверенном тебе автомобиле, как о своём собственном, то отряд «Клуни» с радостью примет тебя в свою семью. В обязанности водителя входит: экплуатация боевого автомобиля, как собственного; перевозка военных грузов; доставка боевых товарищей на "Ноль" и обратно.
""")
    elif message.text == 'Штурмовик':
        photo_url = 'https://github.com/ClooneySquad/test/blob/1d7155ca09993fca84671531d491ac638e7e27bf/ScriptData/SkriptMedia/Asshole.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, """Отряд «Клуни» приглашает специалистов по категории «Штурмовик». Если судьба России для тебя имеет значение, и ты готов встать в строй героев-защитников своей Родины, наша боевая семья примет тебя. 
Нет опыта работы - старшие и опытные товарищи за 3-х недельный курс обучат тебя всему, что пригодится на поле боя. 
Каждый боец отряд «Клуни» с оружием в руках отстаивает право наших предков на землю Донбасса и Малороссии. Это наша земля и м ы готовы за неё бороться.
""")
    elif message.text == 'Медик':
        photo_url = 'https://github.com/ClooneySquad/test/blob/91fe64016bdfb6ad626bc29e69eaf303f6866591/ScriptData/SkriptMedia/medic.jpg?raw=true'
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, """Отряд «Клуни» приглашает специалистов с медицинским образованием, а именно: фельдшеры и врачи-реаниматологи. 
Ты практикующий студент или опытный медик (врач, фельдшер, медбрат) и готов на практике показать свои знания и умения?
- присоединяйся к боевой и дружной команде!
""")
    elif message.text == 'Назад':
        main_menu(message)

bot.polling()
