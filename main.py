import requests
from datetime import datetime
import os
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

text = input("Please Tell me about the exercise you did: ")
GENDER = "male"
WEIGHT = 60
HEIGHT = 170
AGE = 20

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=header)
results = response.json()
print(results)

SHEETY_ENDPOINT = "https://api.sheety.co/a08202321f292c75750cecec333eb2e7/myWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

header1 = {
    "Authorization": TOKEN
}
for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response1 = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=header1)
    print(response1.json())

