import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

if response.status_code == 200:
    data = response.json()
    print(f"\n{data['joke']}\n")
else:
    print("Failed to fetch a joke. Status code:", response.status_code)
