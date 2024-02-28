import requests
import json
import os

while True:
    city = (input("Enter the city: ")).lower()
    if city == "exit":
        command = f"say Goodbye"
        os.system(command)
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=93ee46c50cb847bfb8f212702242702&q={city}"
    response = requests.get(url)
    weatherDic = json.loads(response.text)
    temp = weatherDic['current']['temp_c']
    command = f"say The temperature in {city} is {temp} degrees celsius"
    os.system(command)
    print(f"The temperature in {city} is {temp} degrees celsius")

