video_dictionary = {
    "01d": "/static/images/clear.gif",
    "02d": "/static/images/clear.gif",
    "03d": "/static/images/cloudy.gif",
    "04d": "/static/images/cloudy.gif",
    "09d": "/static/images/rain.gif",
    "10d": "/static/images/rain.gif",
    "11d": "/static/images/rain.gif",
    "50d": "/static/images/rain.gif",
}
def video(icon_code)->'video':
    return video_dictionary[icon_code]