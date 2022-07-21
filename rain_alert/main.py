import requests
from twilio.rest import Client

account_sid = "AC70f6ba03952ae76e69134b79fd7c0a31"
auth_token = "e0b329a9481c0883253e04cb27ddab39"


api_key = '2c252bc94358743cf6b644f234116489'
MY_LAT = 51.339695
MY_LONG = 12.373075
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for hour in data['hourly'][:12]:
    condition_code = hour['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        from_= '+19704894858',
        to='+2349033234055'
    )
    print(message.status)