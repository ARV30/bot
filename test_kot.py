import telebot
from telebot import types

# Установка токена вашего бота
bot = telebot.TeleBot("*********")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем объект клавиатуры
    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    # Создаем кнопки выбора
    button1 = types.KeyboardButton(text="Привет")
    button2 = types.KeyboardButton(text="Пока")

    # Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2)

    # Отправляем приветственное сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Я кот.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Обрабатываем нажатие кнопок выбора
    if message.text == "Привет":
        bot.reply_to(message, "Ну привет, лучше нажми кнопку пока")
    elif message.text == "Пока":
        bot.reply_to(message, "Молодец")

# Запуск приложения
bot.polling()

