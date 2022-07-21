import requests
from datetime import datetime
MY_LAT = 6.501725
MY_LNG = 3.395709
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response)
# response.raise_for_status()
# data = response.json()['iss_position']
# #print(data)
# longitude = data['longitude']
# latitude = data['latitude']
# iss_position = (latitude, longitude)
# print(iss_position)
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted':0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
#print(sunrise.split('T')[1].split(':')[0])
print(sunset)
time_now = datetime.now()
print(time_now.hour)
