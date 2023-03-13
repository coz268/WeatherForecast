import requests

API_KEY = 'your_api_key_here'
CITY = 'New York'

url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

for forecast in data['list']:
    date_time = forecast['dt_txt']
    temp = forecast['main']['temp']
    weather_desc = forecast['weather'][0]['description']
    print(f'{date_time}: {temp} C, {weather_desc}')
