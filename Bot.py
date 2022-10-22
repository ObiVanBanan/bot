#-UTF-8
import requests
import datetime
from config import token, token_ow
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from transliterate import translit


token = '5618901438:AAH3pLXyAOT4fWurGRktCwflFpfLzfaTIbU'
token_ow = 'c63a1ed9c9935eefab960f33dfe1c166'


bot = Bot(token=token)
dp = Dispatcher(bot)




# Функция, обрабатывающая команду /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.Message):
    # while True:
        text = message.text.replace('/', '')
        text = translit(text, language_code='ru', reversed=True)
        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={text}&appid={token_ow}&units=metric"
            )
            data = r.json()
            
            city = data["name"]
            cur_weather = data["main"]["temp"]



            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])

            await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n"
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                f"***Хорошего дня!***"
                )

        except:
            await message.reply("\U00002620 Проверьте название города \U00002620")
        # time.sleep(1)

                
            # while True:
            #     bot.send_message(m.chat.id,'lox')  # типа отправляешь сообщение
            #     time.sleep(1)  # останавливает выполнение кода на минуту


if __name__ == '__main__':
    executor.start_polling(dp)


# anecdot_2 = []

# def configure_logging():
#     log = logging.getLogger('bot')

#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(logging.Formatter(
#     '%(asctime)s %(levelname)s %(message)s'
#     ))

#     file_handler = logging.FileHandler('bot.log', 'w', 'utf-8')
#     file_handler.setFormatter(logging.Formatter(
#     '%(asctime)s %(levelname)s %(message)s'
#     ))
    
#     log.addHandler(stream_handler)
#     log.addHandler(file_handler)

#     log.setLevel(logging.INFO)
#     stream_handler.setLevel(logging.DEBUG)
#     file_handler.setLevel(logging.DEBUG)



# def joke_url():
#     res = requests.get('https://anekdoty.ru/pro-klounov/')
#     soup = bs(res.text, 'html.parser')
#     for joke in soup.find_all('p'):
#         anecdot_2.append(joke.text)

#     rd = random.randint(0, len(anecdot_2))
#     return anecdot_2[rd]




# bot = telebot.TeleBot(config.token)



# @bot.message_handler(commands=["анек"])
# def anecdot(m):
# 	bot.send_message(m.chat.id, joke_url())



# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)


# if __name__ == '__main__':
#     configure_logging()
#     bot.infinity_polling()



# Создаем экземпляр бота



