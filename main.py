import requests
import datetime
APP_ID= "97da513b"
APP_KEY="a7358f5f27dd4d5386179feab57b1f06"


headers =  {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
    "Content" : "json"
}
params = {
 "query": input("Tell me which excercise you did: "),
 "gender":"male",
 "weight_kg":71,
 "height_cm":177,
 "age":20
}
req = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
print(req.json())
today = datetime.datetime.now()
print(today)
headers_sheets = {"Authorization": "Bearer 3534545345456456576578658658yhghcgjtj"}
for t in req.json()["exercises"]:
    sheets_params = {
        "workout": {
        "date": str(today.strftime("%d/%m/%Y")),
        "time": str(today.strftime("%H:%M:%S")),
        "exercise" : t["user_input"],
        "duration" : t["duration_min"],
        "calories" : t["nf_calories"]
        }
    }
    post_sheet = requests.post(url="https://api.sheety.co/0c3da5238a160698139afe44dfbab864/myWorkouts/workouts", json=sheets_params, headers=headers_sheets)
    print(post_sheet.text)