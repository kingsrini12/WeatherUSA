# Python program to find current
# weather details of any city

import requests
import json
import boto3
from datetime import datetime

# Enter your API key here
api_key = "41b665179a15eed336322797d5a593b9"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# Give city name
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

# city is not found
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    weather_data = str(current_temperature) + ',' + str(current_pressure) + ',' + str(current_humidity) + ',' + \
                   str(weather_description)
    print(weather_data)
    weather_data = 'date,temp,pressure,humidity,description' + '\n' + datetime.strftime(datetime.now(), '%Y%m%d') + \
                   ',' + weather_data
    s3 = boto3.resource('s3')
    object = s3.Object('weatherusa', f'{city_name}.txt')
    object.put(Body=weather_data)
else:
    print(" City Not Found ")




