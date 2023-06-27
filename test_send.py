import requests

res = requests.post("http://127.0.0.1:5051/login", json={"username": 1, "password": 12})
print(res.json())  # {'foo': 1, 'age': 12, 'name': 'xiao123'}