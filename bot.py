import telebot
import requests
from requests import get
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot('1346403365:AAGGHqEoYLl8q9SmleX8lXsDv5soyAxBzwA')

r = requests.get('https://sinoptik.ua/погода-богородск')
r.encoding = 'windows-1251'
html=BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min_now = el.select('.temperature .min')[0].text
    t_max_now = el.select('.temperature .max')[0].text
    descriprion_now = el.select('.wDescription .description')[0].text
    wether_now = el.select('.weatherIco')[0].get('title')
    #photo = el.select('.weatherIco .weatherImg')[0].get('src')
    t_0_00 = el.select('.temperature .p1')[0].text
    t_3_00 = el.select('.temperature .p2')[0].text
    t_6_00 = el.select('.temperature .p3')[0].text
    t_9_00 = el.select('.temperature .p4')[0].text
    t_12_00 = el.select('.temperature .p5')[0].text
    t_15_00 = el.select('.temperature .p6')[0].text
    t_18_00 = el.select('.temperature .p7')[0].text
    t_21_00 = el.select('.temperature .p8')[0].text
    t_feels_0_00 = el.select('.temperatureSens .p1')[0].text
    t_feels_3_00 = el.select('.temperatureSens .p2')[0].text
    t_feels_6_00 = el.select('.temperatureSens .p3')[0].text
    t_feels_9_00 = el.select('.temperatureSens .p4')[0].text
    t_feels_12_00 = el.select('.temperatureSens .p5')[0].text
    t_feels_15_00 = el.select('.temperatureSens .p6')[0].text
    t_feels_18_00 = el.select('.temperatureSens .p7')[0].text
    t_feels_21_00 = el.select('.temperatureSens .p8')[0].text
    t_description_0_00 = el.select('.weatherIcoS .p1 .weatherIco ')[0].get('title')
    t_description_3_00 = el.select('.weatherIcoS .p2 .weatherIco ')[0].get('title')
    t_description_6_00 = el.select('.weatherIcoS .p3 .weatherIco ')[0].get('title')
    t_description_9_00 = el.select('.weatherIcoS .p4 .weatherIco ')[0].get('title')
    t_description_12_00 = el.select('.weatherIcoS .p5 .weatherIco ')[0].get('title')
    t_description_15_00 = el.select('.weatherIcoS .p6 .weatherIco ')[0].get('title')
    t_description_18_00 = el.select('.weatherIcoS .p7 .weatherIco ')[0].get('title')
    t_description_21_00 = el.select('.weatherIcoS .p8 .weatherIco ')[0].get('title')
    time_rise = el.select('.infoDaylight')[0].text
    temp_now = el.select('.lSide .imgBlock .today-temp')[0].text
    day_link = el.select('.day-link')[0].text 
    day = el.select('.tabs .main .date ')[0].text
    month = el.select('.tabs .main .month')[0].text


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, я покажу тебе погоду в Богородске, напиши /info') 



@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Cейчас на улице  '+ temp_now + '\n'+ '\n'
                                        +'Погода сегодня: ('+day +' '+ month + ' - '+ day_link + ')\n' 
                                        + t_min_now + ', '+ t_max_now 
                                        + ',' + '\n' + wether_now 
                                        + '\n'+'\n'+ descriprion_now +
                                        '\n'+'\n'+
                                        'Почасовая погода:'+ '\n'+
                                        'Время  '+'Температура '+ 'Ощущается'+'\n'+
                                         '0:00 :     '+ t_0_00 + '                    '+t_feels_0_00 +"  "+t_description_0_00 +'\n'+
                                         '3:00 :     '+ t_3_00 + '                    '+t_feels_3_00 +"  "+t_description_3_00 +'\n'+
                                         '6:00 :     '+ t_6_00 + '                    '+t_feels_6_00 +"  "+t_description_6_00 +'\n'+
                                         '9:00 :     '+ t_9_00 + '                    '+t_feels_9_00 +"  "+t_description_9_00 +'\n'+
                                         '12:00 :     '+ t_12_00 + '                    '+t_feels_12_00 +"  "+t_description_12_00 +'\n'+
                                         '15:00 :     '+ t_15_00 + '                    '+t_feels_15_00 +"  "+t_description_15_00 +'\n'+
                                         '18:00 :     '+ t_18_00 + '                    '+t_feels_18_00 +"  "+t_description_18_00 +'\n'+
                                         '21:00 :     '+ t_21_00 + '                    '+t_feels_21_00 +"  "+t_description_21_00 +'\n'+
                                         '\n'+
                                         time_rise[:13]+' '+ u'\U0001F31D'  +'\n'+time_rise[13:] + ' ' + u'\U0001F31A'                                    
                                         )
    #bot.send_photo(message.chat.id, get('http:'+photo).content)


if __name__ == '__main__':
    bot.polling(none_stop=True)

