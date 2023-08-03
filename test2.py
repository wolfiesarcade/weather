import requests
import json
import datetime
import time
import math


def loop() -> json:
    while True:
        city = "New York"
        api_key = "bc5ef4c4fdcb0080ee220ad05699e411"
        openWeatherUrl = (
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )
        openWeatherResponse = requests.get(openWeatherUrl)
        openWeatherResponse_json = openWeatherResponse.json()
        #print(openWeatherResponse_json)
        unixTimeStamp = int(openWeatherResponse_json["dt"])
        print(unixTimeStamp)
        unixTimeStamp_string= f'"{str(unixTimeStamp)}"'
        print(unixTimeStamp_string)
        dictionaryLocator = unixTimeStamp - 43200
        temperature = openWeatherResponse_json["main"]["temp"]
        farhConversion = round((temperature - 273.15) * 9 / 5 + 32)

        responseDict = {
            unixTimeStamp: [{
                "temperature": farhConversion,
                "humidity": openWeatherResponse_json["main"]["humidity"],
                "icon": openWeatherResponse_json["weather"][0]["icon"],
                "description": openWeatherResponse_json["weather"][0]["description"]
            }]
        }
        #print(responseDict[unixTimeStamp][0]['temperature']) 

        # open a json file for writing data into
        with open ("fileResponse.json", "a") as outFile:

        # extract the specific data from the openweather api  and store it as a JSON
            json.dump(responseDict, outFile)
            time.sleep(3)

        with open("fileResponse.json", "r") as outFile:
            data = json.load(outFile)
            print(data[unixTimeStamp_string])#THIS IS THE ISSUE. THIS GARBAGE RIGHT #HERE. IVE TRIED IT WITH BOTH THE PURE VALUE AND THE INTEGER AND I JUST CANT #ACESS WHAT I WANT
        time.sleep(3600)


print(loop())
