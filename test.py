import requests

api_key = 'bc5ef4c4fdcb0080ee220ad05699e411'


city = 'New York'


url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    print(data)

    # Extract the relevant information from the response
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    # Print the weather information
    print(f'Temperature: {temperature} K')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}')
else:
    print('Error:', response.status_code)