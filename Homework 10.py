import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather
            (date_time TEXT, temperature REAL)''')

url = 'https://ua.sinoptik.ua/погода-київ'
response = requests.get(url)

if response.status_code == 200:
   html = response.content
else:
   print('Не вдалося отримати сторінку')


soup = BeautifulSoup(html, 'html.parser')
weather_today = soup.find('p', {'class': 'today-temp'})

if weather_today:
    today_temperature = int(weather_today.getText()[:-2])
    print(f"Температура сьогодні: {today_temperature}°C")
    temperature = today_temperature
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Час зараз: {date_time}")

    c.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))
    conn.commit()
else:
    print('Не вдалося знайти інформацію про погоду')

conn.close()

