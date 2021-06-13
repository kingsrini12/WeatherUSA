# Python program to find current  weather details of any city and PUSH to S3

import requests
import json
import boto3
from datetime import datetime
def weatherreport(x,city_name):
    # parsing all the variables from JSON
    coord = x["coord"]
    current_coordinates = str(coord["lon"]) + ',' + str(coord["lat"])

    weather = x["weather"]
    current_weather = str(weather[0]["id"]) + ',' +  str(weather[0]["main"]) \
    + ',' + str(weather[0]["description"]) + ',' +   str(weather[0]["icon"])

    current_base = str(x["base"])

    main = x["main"]
    current_main = str(main["temp"])     + ',' + str(main["feels_like"]) \
    +  ','  + str(main["temp_min"]) \
    + ',' + str(main["temp_max"])     + ',' + str(main["pressure"]) \
    + ',' + str(main["humidity"])

    current_visibility=str(x["visibility"])

    wind = x["wind"]
    current_speed = str(wind["speed"])  + ',' + str(wind["deg"])  #+ ',' + str(wind["gust"])

    clouds = x["clouds"]
    current_all = str(clouds["all"])

    current_dt = str(x["dt"])

    sys = x["sys"]
    current_sys = str(sys['type']) + ',' +  str(sys["id"]) + ',' +  str(sys["sunrise"]) + ',' +  \
                  str(sys["sunset"])

    current_timezone = str(x["timezone"])
    current_tz_id = str(x["id"])
    current_name = str(x["name"])
    current_cod = str(x["cod"])

    weather_data = current_coordinates + ',' + current_weather  + ',' + current_base + ',' + current_main + ',' + current_visibility + ',' + \
                   current_speed + ',' + current_all + current_dt + ',' + current_sys + ',' + current_timezone + ',' + \
                   current_tz_id + ',' + current_name + ',' + current_cod


    weather_data = 'LoadDate,longitude, latitude,id,main,description,icon,base,temp,feels_like,temp_min,temp_max,pressure,humidity,' \
                   'visibility,speed,deg,ID1,cloudsAll,ID,sunrise,sunset,timezone,ID,name,cod ' + '\n' + datetime.strftime(datetime.now(), '%Y%m%d') + \
                   ',' + weather_data

    s3 = boto3.resource('s3')
    object = s3.Object('weatherusa', f'{city_name}.txt')
    object.put(Body=weather_data)

# Enter your API key here
api_key = "41b665179a15eed336322797d5a593b9"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# Give city name
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
complete_url_detroit = base_url + "appid=" + api_key + "&q=Detroit"
response = requests.get(complete_url)
response_detroit = requests.get(complete_url)
print(complete_url)
print(complete_url_detroit)
x = response.json()
x_detroit = response_detroit.json()
#print(x)

# city is not found
if x["cod"] != "404":
    weatherreport(x,city_name)
    weatherreport(x_detroit,'Detroit')
else:
    print(" City Not Found ")
