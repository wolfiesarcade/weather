import requests
from icons import icons, icon_dictionary
# from videos import video, video_dictionary
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    api_key = "bc5ef4c4fdcb0080ee220ad05699e411"
    city = "New York"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    dateurl = f"http://worldtimeapi.org/api/timezone/America/New_York"
    response = requests.get(url)
    dateresponse = requests.get(dateurl)
    date = dateresponse.json()

    if response.status_code == 200:
        data = response.json()

        # Extract the relevant information from the response
        temperature = data["main"]["temp"]
        farh= int((temperature - 273.15) * 9 // 5 + 32)
        celsius = int(temperature - 273.15)
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        icondata = data["weather"][0]["icon"]
        iconexecute=icons(icondata)
        # videoexecute=video(icondata)

        # Print the weather information
        weather = {
            "city": city,
            "Temperature": temperature,
            "Humidity": humidity,
            "Description": description,
            "icon": icondata,
        }
        print(weather)
    else:
        print("Error:", response.status_code)

    return render_template("weather.html", weather=weather, celsius=celsius, farh=farh, temperature=temperature, iconexecute=iconexecute)


@app.route("/result/<cityname>")
def cityName(cityname):
    return render_template("city.html", cityname=cityname)
