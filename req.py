import requests
r = requests.post("http://bc9e436f.ngrok.io/sms", data={'From': '+918281958692', 'Body': '45245-13'})
print(r.status_code, r.reason)