import os
import requests

from twilio.rest import Client
from decouple import config

OWM = "https://api.openweathermap.org/data/3.0/onecall"
api_key = config("OWM_API_KEY")
account_sid = config("ACC_SID")
auth_token = config("AUTH_TOKEN")

coordinates = [45.5031824,-73.5698065]

parameters = {
    "lat": coordinates[0],
    "lon": coordinates[1],
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(
    url = OWM,
    params = parameters
)

response.raise_for_status()

data = response.json()

hourly_weather_data = data["hourly"]

morning_weather = [hourly_weather_data for data in range(11)]

morning_hourly_forcast_list = []
for index in range(11):
    forcast = morning_weather[index][0]["weather"][0]["id"]
    morning_hourly_forcast_list.append(int(forcast))

will_rain = False

for condition_code in morning_hourly_forcast_list:
    if condition_code < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
            body = "It's going to rain today. Remember to bring an ☔",
            from_ = config("PHONE_FROM"),
            to = config("PHONE_TO")
        )
    print(message.status)

else:
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
            body = "Ahoy, Clear skies ahead! 🌞",
            from_ = config("PHONE_FROM"),
            to = config("PHONE_TO")
        )
    print(message.status)