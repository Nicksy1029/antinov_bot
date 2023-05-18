
import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5488026909:AAGWNuDbNhu6SPJaCEjMOG3RLzO9v1FxXNs')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создаем кнопки
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Привет')
    button2 = types.KeyboardButton('Пока')
    # Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2)
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_handler(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()