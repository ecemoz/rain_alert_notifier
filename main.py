import requests
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "556db17e41ef5adf1384dee6ffa3bd3e"

account_sid= "ABCDEFGHKJDH"
auth_token= "your_auth_token"

weather_params = {
    "lat":41.44431,
    "lon":27.92194,
    "appid": api_key,
    "cnt":4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Please bring your umbrella",
        from_="+15017122661",
        to="+15558675310"
    )
    print(message.status)

def send_email():
    email_address = "seninmailin@gmail.com"
    email_password = "uygulama_sifresi"
    msg = EmailMessage()
    msg['Subject'] = "Hava Durumu Uyarısı ☔"
    msg['From'] = email_address
    msg['To'] = "hedefmail@ornek.com"
    msg.set_content("Bugün yağmur bekleniyor. Lütfen şemsiyeni almayı unutma!")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("E-posta gönderildi.")