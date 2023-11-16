
import telebot
import aiogram
import requests


bot = telebot.TeleBot('6920490756:AAEIQ8rkBMNCd_rRlcISTkj0JFIyFJDvt7E')


start_txt = 'Привет! Это бот цифрик, но пока он может лишь сказать погоду в нашем городе. \n\nПросто нажми на кнопку'





@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def weather(message):

  city = "Кемерово"

  url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

  weather_data = requests.get(url).json()
  print(weather_data)

  temperature = round(weather_data['main']['temp'])
  temperature_feels = round(weather_data['main']['feels_like'])

  w_now = 'Сейчас в ' + city + ' ' + str(temperature) + ' °C'
  w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'

  bot.send_message(message.from_user.id, w_now)
  bot.send_message(message.from_user.id, w_feels)

  wind_speed = round(weather_data['wind']['speed'])
  if wind_speed < 5:
      bot.send_message(message.from_user.id, '✅ Погода хорошая, ветра почти нет')
  elif wind_speed < 10:
      bot.send_message(message.from_user.id, '🤔 На улице ветрено, оденьтесь чуть теплее')
  elif wind_speed < 20:
      bot.send_message(message.from_user.id, '❗️ Ветер очень сильный, будьте осторожны, выходя из дома')
  else:
      bot.send_message(message.from_user.id, '❌ На улице шторм, на улицу лучше не выходить')


if __name__ == '__main__':
    while True:

        try:
            bot.polling(none_stop=True, interval=0)

        except Exception as e:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')

bot.polling(none_stop=True)
