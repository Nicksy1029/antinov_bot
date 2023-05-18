import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5488026909:AAGWNuDbNhu6SPJaCEjMOG3RLzO9v1FxXNs')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создаем кнопки
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Привет', callback_data='hello')
    button2 = types.InlineKeyboardButton(text='Пока', callback_data='goodbye')
    # Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2)
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'hello':
        bot.send_message(call.message.chat.id, 'Привет!')
    elif call.data == 'goodbye':
        bot.send_message(call.message.chat.id, 'Пока!')


# Запуск бота
bot.polling()