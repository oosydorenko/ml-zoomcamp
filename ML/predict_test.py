import requests

url = 'http://localhost:9696/predict'

client1 = {"job": "unknown", "duration": 270, "poutcome": "failure"}
client2 = {"job": "retired", "duration": 445, "poutcome": "success"}

response1 = requests.post(url, json=client1).json()
print(f'client:{client1}, response:{response1}')

response2 = requests.post(url, json=client2).json()
print(f'client:{client2}, response:{response2}')