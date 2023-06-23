import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        icon= data["weather"][0]["icon"]

        # Print the weather information
        weather = {
            'city': city,
            'Temperature': temperature,
            'Humidity': humidity,
            'Description': description,
            'icon' :  icon 
        }
        print(weather)
    else:
        print("Error:", response.status_code)

    return render_template("weather.html", weather=weather)
