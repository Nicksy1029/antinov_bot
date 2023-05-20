
import telebot
from telebot import types
import os, sys

# Создаем экземпляр бота
bot = telebot.TeleBot('5488026909:AAGWNuDbNhu6SPJaCEjMOG3RLzO9v1FxXNs')

#Текст
tochka=('\n- Точка - это объект без размера, который обозначается заглавной буквой латинского алфавита.')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создаем кнопки
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Формулы', callback_data='hello')
    button2 = types.InlineKeyboardButton(text='Рецепты', callback_data='goodbye')
    # Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2)
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    #Кнопки предметов
    keyboard2 = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton(text='Геометрия', callback_data='geom')
    button4 = types.InlineKeyboardButton(text='Алгебра', callback_data='algeb')
    button5 = types.InlineKeyboardButton(text='Физика', callback_data='phisik')
    keyboard2.add(button3, button5, button4)


    #Кнопки времён еды
    keyboard3 = types.InlineKeyboardMarkup()
    button6 = types.InlineKeyboardButton(text='Завтрак', callback_data='zavtrak')
    button7 = types.InlineKeyboardButton(text='Обед', callback_data='obed')
    button8 = types.InlineKeyboardButton(text='Ужин', callback_data='uzin')
    button9 = types.InlineKeyboardButton(text='Полдник', callback_data='slad')
    keyboard3.add(button6, button7, button8, button9)


    #Кнопки завтрака
    keyboard4 = types.InlineKeyboardMarkup()
    baton1 = types.InlineKeyboardButton(text='1', callback_data='zav1')
    baton2 = types.InlineKeyboardButton(text='2', callback_data='zav2')
    baton3 = types.InlineKeyboardButton(text='3', callback_data='zav3')
    baton4 = types.InlineKeyboardButton(text='4', callback_data='zav4')
    baton5 = types.InlineKeyboardButton(text='5', callback_data='zav5')
    keyboard4.add(baton1, baton2, baton3, baton4, baton5)


    #Кнопки обеда
    keyboard5 = types.InlineKeyboardMarkup()
    kod1 = types.InlineKeyboardButton(text='1', callback_data='ob1')
    kod2 = types.InlineKeyboardButton(text='2', callback_data='ob2')
    kod3 = types.InlineKeyboardButton(text='3', callback_data='ob3')
    kod4 = types.InlineKeyboardButton(text='4', callback_data='ob4')
    kod5 = types.InlineKeyboardButton(text='5', callback_data='ob5')
    keyboard5.add(kod1, kod2, kod3, kod4, kod5)


    #Кнопки ужина
    keyboard6 = types.InlineKeyboardMarkup()
    vard1 = types.InlineKeyboardButton(text='1', callback_data='uz1')
    vard2 = types.InlineKeyboardButton(text='2', callback_data='uz2')
    vard3 = types.InlineKeyboardButton(text='3', callback_data='uz3')
    vard4 = types.InlineKeyboardButton(text='4', callback_data='uz4')
    vard5 = types.InlineKeyboardButton(text='5', callback_data='uz5')
    keyboard6.add(vard1, vard2, vard3, vard4, vard5)


    #Кнопки полдника
    keyboard7 = types.InlineKeyboardMarkup()
    kek1 = types.InlineKeyboardButton(text='1', callback_data='pol1')
    kek2 = types.InlineKeyboardButton(text='2', callback_data='pol2')
    kek3 = types.InlineKeyboardButton(text='3', callback_data='pol3')
    kek4 = types.InlineKeyboardButton(text='4', callback_data='pol4')
    kek5 = types.InlineKeyboardButton(text='5', callback_data='pol5')
    keyboard7.add(kek1, kek2, kek3, kek4, kek5)


    #Формулы
    if call.data == 'hello':
        bot.send_message(call.message.chat.id, 'Какой профиль?', reply_markup=keyboard2)

    if call.data == 'geom':
        bot.send_message(call.message.chat.id, 'ТРЕУГОЛЬНИКИ:\nS = √(p(p - a)(p - b)(p - c)), где p - полупериметр\nS=ah*0,5\nS=0,5*a*b*sinC\nТеорема Пифагора: c² = a² + b²\nЧЕТЫРЁХУГОЛЬНИКИ:\nS трапеции = (a + b)h / 2\nS параллелограмма = ah\nКРУГ:\nДлина окружности L = 2πr\nS = πr²\nСектор круга: S = (a/360) * πr²')

    if call.data == 'algeb':
        bot.send_message(call.message.chat.id, 'не знаю пока')
    
    if call.data == 'phisik':
        bot.send_message(call.message.chat.id, 'E=mc квадрат')


    #Рецепты
    if call.data == 'goodbye':
        bot.send_message(call.message.chat.id, 'Время?', reply_markup=keyboard3)
    

    #Завтрак
    if call.data == 'zavtrak':
        bot.send_message(call.message.chat.id, 'Выбери от 1 до 5', reply_markup=keyboard4)

    if call.data == 'zav1':
        bot.send_message(call.message.chat.id, 'завтрак1')

    if call.data == 'zav2':
        bot.send_message(call.message.chat.id, 'завтрак2')

    if call.data == 'zav3':
        bot.send_message(call.message.chat.id, 'завтрак3')

    if call.data == 'zav4':
        bot.send_message(call.message.chat.id, 'завтрак4')

    if call.data == 'zav5':
        bot.send_message(call.message.chat.id, 'завтрак5')


    #Обед
    if call.data == 'obed':
        bot.send_message(call.message.chat.id, 'Выбери от 1 до 5', reply_markup=keyboard5)

    if call.data == 'ob1':
        bot.send_message(call.message.chat.id, 'обед1')

    if call.data == 'ob2':
        bot.send_message(call.message.chat.id, 'обед2')

    if call.data == 'ob3':
        bot.send_message(call.message.chat.id, 'обед3')

    if call.data == 'ob4':
        bot.send_message(call.message.chat.id, 'обед4')

    if call.data == 'ob5':
        bot.send_message(call.message.chat.id, 'обед5')


    #Ужин
    if call.data == 'uzin':
        bot.send_message(call.message.chat.id, 'Выбери от 1 до 5', reply_markup=keyboard6)

    if call.data == 'uz1':
        bot.send_message(call.message.chat.id, 'ужин1')

    if call.data == 'uz2':
        bot.send_message(call.message.chat.id, 'ужин2')

    if call.data == 'uz3':
        bot.send_message(call.message.chat.id, 'ужин3')

    if call.data == 'uz4':
        bot.send_message(call.message.chat.id, 'ужин4')

    if call.data == 'uz5':
        bot.send_message(call.message.chat.id, 'ужин5')


    #Полдник
    if call.data == 'slad':
        bot.send_message(call.message.chat.id, 'Выбери от 1 до 5', reply_markup=keyboard7)

    if call.data == 'pol1':
        bot.send_message(call.message.chat.id, 'полдник1')

    if call.data == 'pol2':
        bot.send_message(call.message.chat.id, 'полдник2')

    if call.data == 'pol3':
        bot.send_message(call.message.chat.id, 'полдник3')

    if call.data == 'pol4':
        bot.send_message(call.message.chat.id, 'полдник4')

    if call.data == 'pol5':
        bot.send_message(call.message.chat.id, 'полдник5')    



# Запуск бота
bot.polling()