import telegram
from telegram import types
from telegram.types import KeyboardButton

bot = telegram.Bot('1761768781:AAG3WIDomiWAuPEMOyr9y9wLsVE5CLpVOlo')

#вебсайт

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='http://islam.ru/content/veroeshenie/55127?utm_referrer=https%3A%2F%2Fzen.yandex.com&utm_campaign=dbr'))
    bot.send_message(message.chat.id,"Отличный выбор, нажмите на кнопку чтоб прочитать статью", parse_mode='html', reply_markup=markup)





#начальный

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, row_width=5)
    btn1 = KeyboardButton = types.KeyboardButton('Рамадан - месяц надежды')
    btn2 = types.KeyboardButton('4 награды в месяц Рамадан')
    btn3 = types.KeyboardButton('Нашид “Рамадану я Рамадан')
    markup.add(btn1 , btn2 , btn3 )

    send_mess = f"<b> Мир вам ! {message.from_user.first_name} {message.from_user.last_name} </b>\nРекомендую посмотреть наш последний ролик , Рамадан - месяц надежды "
    bot.send_message(message.chat.id,  send_mess,  parse_mode='html', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def func (message):
    get_message_bot = message.text.strip().lower()

#кнопка1

    if message.text == 'Рамадан - месяц надежды':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True, row_width=5 )
        bot.send_message(message.chat.id, text = 'Приятного просмотра ! https://youtu.be/MuHnPd6UJGI ', parse_mode='html', reply_markup=markup)

    if message.text == 'Нашид “Рамадану я Рамадан':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True, row_width=5 )
        bot.send_message(message.chat.id, text='Приятного просмотра ! https://www.youtube.com/watch?v=P10zaYYuBa4 ',
                         parse_mode='html', reply_markup=markup)







#кнопка3


    elif message.text == '4 награды в месяц Рамадан':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True, row_width=5 )
        btn1: KeyboardButton = types.KeyboardButton('Рамадан - месяц надежды')
        btn2 = types.KeyboardButton('4 награды в месяц Рамадан ')
        bot.send_message(message.chat.id, text = 'Приятного чтения ! http://islam.ru/content/veroeshenie/55127?utm_referrer=https%3A%2F%2Fzen.yandex.com&utm_campaign=dbr', parse_mode='html', reply_markup=markup)










if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(-0)
            print(e)