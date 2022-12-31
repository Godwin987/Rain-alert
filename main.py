import pydoc
import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = os.getenv('api_key')

my_email = os.getenv('my_email')
password = os.getenv('password')
BOT_TOKEN = os.getenv('bot_token')
BOT_CHATID = os.getenv('bot_chatID')

parameters = {
    "lat": -5.041480,
    "lon": 18.819140,
    "appid": api_key,
    "exclude": "current,daily"
}


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


# def send_to_telegram(message):
#     apiToken = '5664737899:AAEZX-t3GHLljycZpueIgcjEycNWEgXKTk4'
#     chatID = '1999930604'
#     apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
#
#     try:
#         response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
#         print(response.text)
#     except Exception as e:
#         print(e)


response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
weather_id = 0
for hour in range(0, 12):
    weather_id = weather_data["hourly"][hour]["weather"][0]["id"]
    if weather_id < 700:
        weather_id = weather_id
if weather_id < 700:
    # with smtplib.SMTP(host="smtp.gmail.com") as connection:
    #     connection.ehlo()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email, to_addrs="pythontutorial40@gmail.com",
    #                         msg="Subject:Weather forecast\n\n It's going to be a rainy day. Carry your umbrella☔☔")
    # send_to_telegram("Hello from Python!")
    test = telegram_bot_sendtext("It's going to be a rainy day. Carry your umbrella☔☔")
    print(test)
