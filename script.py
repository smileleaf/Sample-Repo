import requests

r = requests.get("https://cnn.com")
print(r.status_code)
print(r.ok)
print("hamza")
