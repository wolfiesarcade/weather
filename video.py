video_dictionary = {
    "01d": "/static/images/clear.gif",
    "02d": "/static/images/clear.gif",
    "03d": "/static/images/cloudy.gif",
    "04d": "/static/images/cloudy.gif",
    "09d": "/static/images/rain.gif",
    "10d": "/static/images/rain.gif",
    "11d": "/static/images/rain.gif",
    "50d": "/static/images/rain.gif",
    "01n": "/static/images/clear.gif",
    "02n": "/static/images/clear.gif",
    "03n": "/static/images/cloudy.gif",
    "04n": "/static/images/cloudy.gif",
    "09n": "/static/images/rain.gif",
    "10n": "/static/images/rain.gif",
    "11n": "/static/images/rain.gif",
    "50n": "/static/images/rain.gif",
}


def video(icon_code) -> "video":
    return video_dictionary[icon_code]
