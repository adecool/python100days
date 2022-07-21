import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = 51.2
HEIGHT_CM = 135
AGE = 20


API_KEY = "69c11ae70150f245df111b2e567e64c9	"
API_ID = "5158ab87"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/c07c7aa73a171d1ea183a1c636a6d331/workoutTracking/workouts"

headers = {
    "x-app-key" :API_KEY,
    "x-app-id" :API_ID,
}

exercise_params = {
    'query': input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()
print(result)



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:

    sheet_inputs = {
        'workout' : {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=('gen2proff', 'gen2;soul'))
    print(sheet_response.text)

