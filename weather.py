import requests
import os

print("Which weather forecast would you like?\n\n(1) - Current weather\n(2) - 5 day forecast (every 3 hours)")
while True:
    try:
        forecast = int(input("\nEnter your choice here: "))
        if forecast == 1 or forecast == 2:
            break
        else:
            raise ValueError
    except ValueError:
        print("Not a valid choice! Try again!")
city = input("\nEnter city name here: ")

if forecast == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    api_call = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8301dd732a73e8670d3c380f82e92cf0&units=metric"

    json_data = requests.get(api_call).json()

    temperature = json_data["main"]["temp"]
    weather = json_data["weather"][0]["description"]

    print("Current temperature in " + city + " is: " + str(temperature) + " C° with " + weather)
if forecast == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    api_call = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=8301dd732a73e8670d3c380f82e92cf0&units=metric"

    json_data = requests.get(api_call).json()
    lenght = len(json_data["list"])

    for i in range(lenght):
        temperature = json_data["list"][i]["main"]["temp"]
        weather = json_data["list"][i]["weather"][0]["description"]
        date = json_data["list"][i]["dt_txt"]
        print("On " + date + " the temperature will be: " + str(temperature) + " C° with " + weather)


