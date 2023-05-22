import requests

#this is a python code for a HTTP GET request.

url = "https://console.jumpcloud.com/api/systemusers"

# Define parameters for the request
querystring = {"email": "<EMAIL OF USER>"}

# Define headers
headers = {
    "x-org-id": "<YOUR ORG ID>",
    "x-api-key": "<YOUR API KEY>",
    "content-type": "application/json"
}

# Make a GET request to Jumpcloud's API to obtain user's ID with an email
response = requests.request("GET", url, headers=headers, params=querystring)

# Check if there was a successful response and the user exists in Jumpcloud
if response.status_code == 200:
    user = response.json()[0]  # Selects the first match
    user_id = user["_id"]
    print(f"The user {user['username']} will be DELETED.")
    
    # Make a  DELETE request to the Jumpcloud's API
    delete_url = f"https://console.jumpcloud.com/api/systemusers/{user_id}"
    delete_response = requests.request("DELETE", delete_url, headers=headers)
    
    # Check if the deletion was successful
    if delete_response.status_code == 204:
        print(f"The user {user['username']} was deleted successfully.")
    else:
        print(f"Error while deleting the user {user['username']}.")
        print(f"Server Response: {delete_response.text}")
else:
    print(f"User with the email provided not found.")
