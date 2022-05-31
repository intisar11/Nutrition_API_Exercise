import requests


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

print(response.json())
