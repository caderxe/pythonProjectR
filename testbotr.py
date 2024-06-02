import telebot
import time
from telebot import types


# TOKEN
TOKEN = "1761768781:AAG3WIDomiWAuPEMOyr9y9wLsVE5CLpVOlo"

bot = telebot.TeleBot(TOKEN)

#начальный
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Серия 1 | Кто такой дьявол (шайтан) ?')
    btn2 = types.KeyboardButton('Серия 2 | Приёмы и хитрости сатаны')
    btn3 = types.KeyboardButton('Серия 3 | Солдаты Иблиса')
    btn4 = types.KeyboardButton('Серия 4 | Манипуляция сознанием')
    btn5 = types.KeyboardButton('Серия 5 | Где находиться трон Иблиса?')
    btn6 = types.KeyboardButton('Серия 6 | Аль-Масих ад-Даджаль (Антихрист)')
    btn7 = types.KeyboardButton('Серия 7 | Зависимость от социальных сетей')
    btn8 = types.KeyboardButton('Серия 8 | Основы колдовства')
    btn9 = types.KeyboardButton('Серия 9 | Виды колдовства')
    btn10 = types.KeyboardButton('Серия 10 | Влияние телевидения на массы людей')
    btn11 = types.KeyboardButton('Серия 11 | Влияние музыки на людей')
    btn12 = types.KeyboardButton('Серия 12 | Музыка оружие дьявола')
    btn13 = types.KeyboardButton('Серия 13 | Влияние компьютерных игр')
    btn14 = types.KeyboardButton('Серия 14 | Отречение шайтана')
    btn15 = types.KeyboardButton('Серия 15 | Истинная цель феминизма')
    btn16 = types.KeyboardButton('Серия 16 | Порнозависимость')
    btn17 = types.KeyboardButton('Серия 17 | Распространение разврата')
    btn18 = types.KeyboardButton('Серия 18 | Современное образование')
    btn19 = types.KeyboardButton('Серия 19 | Современная наука')
    btn20 = types.KeyboardButton('Серия 20 | Вся правда о ГМО')
    btn21 = types.KeyboardButton('Серия 24 | Величайшая скорбь нашей эпохи')
    btn22 = types.KeyboardButton('Серия 25 | Вся правда о христианстве')
    btn23 = types.KeyboardButton('Серия 26 | Вся правда об Исламе')
    btn24 = types.KeyboardButton('Серия 27 | Нападки на Ислам')
    btn25 = types.KeyboardButton('Серия 28 | Материализм')
    btn26 = types.KeyboardButton('Серия 29 | Дополненная реальность')
    markup.add(btn1 , btn2 , btn3, btn4, btn5, btn6, btn7,
    btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17,
    btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26 )

    send_mess = f"<b> Мир вашему дому  {message.from_user.first_name} {message.from_user.last_name} ! </b>\nРекомендую посмотреть наш последний ролик : Дополненная Реальность "
    bot.send_message(message.chat.id,  send_mess,  parse_mode='html', reply_markup=markup)


#вебсайт

# @bot.message_handler(commands=['website'])
# def open_website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить сайт', url='http://islam.ru/content/veroeshenie/55127?utm_referrer=https%3A%2F%2Fzen.yandex.com&utm_campaign=dbr'))
#     bot.send_message(message.chat.id,"Отличный выбор, нажмите на кнопку чтоб прочитать статью", parse_mode='html', reply_markup=markup)







@bot.message_handler(content_types=['text'])
def func (message):

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Серия 1 | Кто такой дьявол (шайтан) ?')
    btn2 = types.KeyboardButton('Серия 2 | Приёмы и хитрости сатаны')
    btn3 = types.KeyboardButton('Серия 3 | Солдаты Иблиса')
    btn4 = types.KeyboardButton('Серия 4 | Манипуляция сознанием')
    btn5 = types.KeyboardButton('Серия 5 | Где находиться трон Иблиса?')
    btn6 = types.KeyboardButton('Серия 6 | Аль-Масих ад-Даджаль (Антихрист)')
    btn7 = types.KeyboardButton('Серия 7 | Зависимость от социальных сетей')
    btn8 = types.KeyboardButton('Серия 8 | Основы колдовства')
    btn9 = types.KeyboardButton('Серия 9 | Виды колдовства')
    btn10 = types.KeyboardButton('Серия 10 | Влияние телевидения на массы людей')
    btn11 = types.KeyboardButton('Серия 11 | Влияние музыки на людей')
    btn12 = types.KeyboardButton('Серия 12 | Музыка оружие дьявола')
    btn13 = types.KeyboardButton('Серия 13 | Влияние компьютерных игр')
    btn14 = types.KeyboardButton('Серия 14 | Отречение шайтана')
    btn15 = types.KeyboardButton('Серия 15 | Истинная цель феминизма')
    btn16 = types.KeyboardButton('Серия 16 | Порнозависимость')
    btn17 = types.KeyboardButton('Серия 17 | Распространение разврата')
    btn18 = types.KeyboardButton('Серия 18 | Современное образование')
    btn19 = types.KeyboardButton('Серия 19 | Современная наука')
    btn20 = types.KeyboardButton('Серия 20 | Вся правда о ГМО')
    btn21 = types.KeyboardButton('Серия 24 | Величайшая скорбь нашей эпохи')
    btn22 = types.KeyboardButton('Серия 25 | Вся правда о христианстве')
    btn23 = types.KeyboardButton('Серия 26 | Вся правда об Исламе')
    btn24 = types.KeyboardButton('Серия 27 | Нападки на Ислам')
    btn25 = types.KeyboardButton('Серия 28 | Материализм')
    btn26 = types.KeyboardButton('Серия 29 | Дополненная реальность')

    markup.add(btn1 , btn2 , btn3, btn4, btn5, btn6, btn7,
    btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16 ,
    btn17, btn18, btn19, btn20 , btn21, btn22, btn23, btn24, btn25, btn26 )

#кнопка1

    if message.text == 'Серия 1 | Кто такой дьявол (шайтан) ?':
        bot.send_message(message.chat.id, text =
                         'Приятного просмотра ! https://youtu.be/PgjKTIUJ_Tk?si=29et5yriY-3uqL7h ', 
                            parse_mode='html', reply_markup=markup)

    elif message.text == 'Серия 2 | Приёмы и хитрости сатаны':
         bot.send_message(message.chat.id, text=
                          'Приятного просмотра ! https://youtu.be/WnD8mN0r1ss?si=hUT2ttd85iQYim7U ', 
                          parse_mode='html', reply_markup=markup)


#кнопка3


    elif message.text == 'Серия 3 | Солдаты Иблиса':
        bot.send_message(message.chat.id, text =
                         'Приятного просмотра ! https://youtu.be/qrle2VpRuL8?si=V6WhSzecX01JfbGA',
                           parse_mode='html', reply_markup=markup)
    
    
    elif message.text == 'Серия 4 | Манипуляция сознанием':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/aoMgcGqFgsQ?si=T8r1EwuCfmjXGh37',
                           parse_mode='html', reply_markup=markup)
    
    
    elif message.text == 'Серия 5 | Где находиться трон Иблиса?':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/AwIsFJGd4qM?si=4L4m76E4FsmoLEEg',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 6 | Аль-Масих ад-Даджаль (Антихрист)':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/xEXJeSiZKJw?si=HRRfakVrZ5ji0CKx',
                           parse_mode='html', reply_markup=markup)
        
    
    elif message.text == 'Серия 7 | Зависимость от социальных сетей':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/eKGNQe2rRQ8?si=06kRRNKWrMwNRrP6',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 8 | Основы колдовства':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/mPLnJXnLhnI?si=YcnpFJhJGb_h3xr4',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 9 | Виды колдовства':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/RB5dUXKKrZ4?si=nBtaEmGxx7wtLtcZ',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 10 | Влияние телевидения на массы людей':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/ox_Mj1nUeF8?si=o94DqQ7hNyL1yH_X',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 11 | Влияние музыки на людей':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/N_-BMdYFQsk?si=RinHifyroxEiO9HS',
                           parse_mode='html', reply_markup=markup)


    
    elif message.text == 'Серия 12 | Музыка оружие дьявола':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/NcZ3bTIH_rw?si=vevMxLb2cpr2UMxJ',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 13 | Влияние компьютерных игр':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/5kqpmNiOyE0?si=Ul37zkROuYd2uh7S',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 14 | Отречение шайтана':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/DUcpIH0Jcyk?si=KTZ3oluFrs_0sMej',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 15 | Истинная цель феминизма':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/lnkmzAwFWB4?si=spFE5QWhH6RHgfFy',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 16 | Порнозависимость':
        bot.send_message(message.chat.id, text =
                         'https://youtube/UgCoo55BRGQ?si=O-L8CieVUgGWHuOB',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 17 | Распространение разврата':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/3-mcWvLPI2k?si=WtFwyUOW5rJ9HISX',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 18 | Современное образование':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/kndeML7NdoA?si=E2SF5txt_0xsaefv',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 19 | Современная наука':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/NLLoacYVGBU?si=Ko5NTatsZAmk2lMF',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 20 | Вся правда о ГМО':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/hbz1VrtgSOE?si=m2W577y-Ht454LsY',
                           parse_mode='html', reply_markup=markup)
        
    elif message.text == 'Серия 24 | Величайшая скорбь нашей эпохи':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/QjvJJRSsJgs?si=nMcDrQ2tn9QUy-JT',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 25 | Вся правда о христианстве':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/qxUvGzhjuOc?si=Wm86kFGlYANYw5ul',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 26 | Вся правда об Исламе':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/rE6ZVoQrH2s?si=KQjVWHig9pQfclKT',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 27 | Нападки на Ислам':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/XoHqL6qfjvo?si=b0blRart0OY2UWVt',
                           parse_mode='html', reply_markup=markup)
        

    
    
    
    
    
    elif message.text == 'Серия 28 | Материализм (новый секулярный порядок)':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/cW1JKGjHuoA?si=11hK7y2-P06H7grc',
                           parse_mode='html', reply_markup=markup)
        

    elif message.text == 'Серия 29 | Дополненная реальность':
        bot.send_message(message.chat.id, text =
                         'https://youtu.be/pDZKPEzZgFM?si=yxFYOQsSob4RX40U',
                           parse_mode='html', reply_markup=markup)





if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(0)
            print(e)