import requests

api_key = "API-KEY"
url = "https://console.jumpcloud.com/api/v2/usergroups"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": api_key
}

limit = 500
skip = 0
total_groups = 0

while True:
    params = {"limit": limit, "skip": skip}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        break

    user_groups = response.json()
    num_groups = len(user_groups)
    total_groups += num_groups

    for group in user_groups:
        print(group["name"])

    if num_groups < limit:
        break

    skip += limit

print(f"Retrieved {total_groups} user groups.")
