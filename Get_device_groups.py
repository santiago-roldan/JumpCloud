import requests
import json

api_key = "API_KEY"
url = "https://console.jumpcloud.com/api/v2/systemgroups"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    device_groups = json.loads(response.content.decode('utf-8'))
    for group in device_groups:
        print(group["name"])
else:
    print(f"Error: API request failed with status code {response.status_code}")
