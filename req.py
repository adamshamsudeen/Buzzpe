import requests
r = requests.post("http://5daa5bdc.ngrok.io/sms", data={'From': '+918281958692', 'Body': '45245-13'})
print(r.status_code, r.reason)