import telebot
from telebot import types


# TOKEN
TOKEN = "1761768781:AAG3WIDomiWAuPEMOyr9y9wLsVE5CLpVOlo"

bot = telebot.TeleBot(TOKEN)

#начальный
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Рамадан - месяц надежды')
    btn2 = types.KeyboardButton('4 награды в месяц Рамадан')
    btn3 = types.KeyboardButton('Нашид')
    btn4 = types.KeyboardButton('No name')
    btn5 = types.KeyboardButton('No name')
    btn6 = types.KeyboardButton('No name')
    markup.add(btn1 , btn2 , btn3, btn4, btn5, btn6 )

    send_mess = f"<b> Мир вашему дому  {message.from_user.first_name} {message.from_user.last_name} ! </b>\nРекомендую посмотреть наш последний ролик , Рамадан - месяц надежды "
    bot.send_message(message.chat.id,  send_mess,  parse_mode='html', reply_markup=markup)


#вебсайт

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='http://islam.ru/content/veroeshenie/55127?utm_referrer=https%3A%2F%2Fzen.yandex.com&utm_campaign=dbr'))
    bot.send_message(message.chat.id,"Отличный выбор, нажмите на кнопку чтоб прочитать статью", parse_mode='html', reply_markup=markup)







@bot.message_handler(content_types=['text'])
def func (message):
    get_message_bot = message.text.strip().lower()

#кнопка1

    if message.text == 'Рамадан - месяц надежды':
        bot.send_message(message.chat.id, text=
                         'Приятного просмотра ! https://youtu.be/MuHnPd6UJGI ', 
                            parse_mode='html', reply_markup=markup)

    elif message.text == 'Нашид “Рамадану я Рамадан':
         bot.send_message(message.chat.id, text=
                          'Приятного просмотра ! https://www.youtube.com/watch?v=P10zaYYuBa4 ', 
                          parse_mode='html', reply_markup=markup)


#кнопка3


    elif message.text == '4 награды в месяц Рамадан':
        bot.send_message(message.chat.id, text=
                         'Приятного чтения ! http://islam.ru/content/veroeshenie/55127?utm_referrer=https%3A%2F%2Fzen.yandex.com&utm_campaign=dbr',
                           parse_mode='html', reply_markup=markup)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2 )
    btn1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn3 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn4 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn5 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn6 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)






if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep()
            print(e)