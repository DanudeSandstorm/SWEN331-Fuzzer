import requests

base_url = "http://127.0.0.1/"

dvwa = requests.get(base_url)

print(dvwa._content)