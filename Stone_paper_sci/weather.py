import requests
import json
import win32com.client as win32  # Used for Windows text-to-speech
import os

city = input('Enter the name of the city: ')

# Remove extra 'i' in URL after {city}
url = f'http://api.weatherapi.com/v1/current.json?key=a5eb7b136c104474bfb100130250208&q={city}&aqi=yes'

r = requests.get(url)
wdic = json.loads(r.text)

# Get temperature
temperature = wdic['current']['temp_c']
print(f"Current temperature in {city} is {temperature}°C")

# Use Windows speech API (SAPI)
speaker = win32.Dispatch("SAPI.SpVoice")
speaker.Speak(f"The current temperature in {city} is {temperature} degrees Celsius.")
