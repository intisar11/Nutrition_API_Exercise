import requests
from datetime import datetime

app_Id = "e8eca5ad"
API_key = "3a6a6798d25ea61f3512af51af8376de"

Gender = "male"
Height_Cm = 180
Age = 27
Weight_kg = 80


headers ={
    "x-app-id" : app_Id,
    "x-app-key": API_key
}

exercise_text = input("What did you do today?:")

params = {
    "query": exercise_text ,
    "gender": Gender,
    "weight_kg": Weight_kg,
    "height_cm": Height_Cm,
    "age": Age
}
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, json=params, headers=headers)
data = response.json()
print(data)

exercise = (data['exercises'][0]['name'])

Duration = (data['exercises'][0]['duration_min'])

Calories = (data['exercises'][0]['nf_calories'])

date_now = datetime.now().strftime("%d%m%Y")
time_now = datetime.now().strftime("%X")



sheety_data = "https://api.sheety.co/1b804a7375398b54f22f199adbfa614d/copyOfMyWorkouts/workouts"

params = {
    "workout":{
        "date": date_now,
        "time": time_now,
        "excercise": exercise,
        "duration": Duration,
        "calories": Calories
    }
}

response_1 = requests.post(url= sheety_data, json= params)

print(response_1.json())