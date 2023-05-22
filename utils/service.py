import requests
import json
from utils.credentials import *

#This is your main class file, here you can add more methods to manage your Jumpcloud environment
#Remember to replace the values in the file credentials.py with your API key and orgID to make it work properly




class JumpcloudDirector:
    base_url = "https://console.jumpcloud.com/api"
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": api_key,
            "x-org-id": org_id
        }

    def create_user(self, first_name, last_name, username, password):
        endpoint = f"{self.base_url}/systemusers"
        data = {
            "username": username,
            "password": password,
            "email": f"{username}@<DOMAIN.COM>", #replace DOMAIN with your own domain
            "firstname": first_name,
            "lastname": last_name,
            "activated": True,
            "emailVerified": True,
            "allowPublicKey": False,
            "requirePasswordReset": False,
            "requireMfa": True
        }

        try:
            response = requests.post(endpoint, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()
            user_data = response.json()
            return user_data['_id']
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while creating the user: {e}")
            return None



    def update_user(self, email, first_name=None, last_name=None, password=None):
        user_id = self.get_user_id_by_email(email)
        if user_id is None:
            return None
        url = "https://console.jumpcloud.com/api/v2/users/{}".format(user_id)
        payload = {}
        if first_name:
            payload["firstName"] = first_name
        if last_name:
            payload["lastName"] = last_name
        if password:
            payload["password"] = password
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def delete_user(self, email):
        user_id = self.get_user_id_by_email(email)
        if user_id is None:
            return None
        url = "https://console.jumpcloud.com/api/v2/users/{}".format(user_id)
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            print('Error while trying to delete user: {}'.format(response.text))
            return False


    def add_user_to_group(self, user_id, group_id):
        url = f"{self.base_url}/v2/usergroups/{group_id}/members"

        payload = {
            "id": user_id,
            "op": "add",
            "type": "user"
        }

        response = requests.post(url, json=payload, headers=self.headers)

        if response.status_code == 204:
            print(f"User {user_id} added to group {group_id} successfully.")
        else:
            print(f"Error while adding user {user_id} to group {group_id}.")
            print("Debug: API response while adding user to group:")
            print(response.text)

    def get_user_id_by_email(self, email):
        endpoint = f"{self.base_url}/search/systemusers"
        payload = {
            "filter": {
                "email": {
                    "eq": email
                }
            },
            "fields": ["_id"]
        }

        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            users_data = response.json()["results"]
            if len(users_data) > 0:
                return users_data[0]["_id"]
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while retrieving the user ID: {e}")
            return None
        

    def remove_user_from_group(self, email, group_id):
        user_id = self.get_user_id_by_email(email)
        if user_id is None:
            return None
        url = "https://console.jumpcloud.com/api/v2/users/{}/memberof".format(user_id)
        payload = {
            "op": "remove",
            "type": "group",
            "id": group_id
        }
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 204:
            return True
        else:
            return False
    def get_group_members_emails(self, group_name):
        url = f"{self.base_url}/v2/usergroups"
        params = {
            "filter": f"name in {group_name}"
        }

        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            groups = response.json()["results"]
            if len(groups) > 0:
                group_id = groups[0]["_id"]
                members_url = f"{self.base_url}/v2/usergroups/{group_id}/members"
                members_response = requests.get(members_url, headers=self.headers)
                if members_response.status_code == 200:
                    members = members_response.json()["results"]
                    member_emails = [member["email"] for member in members if "email" in member]
                    return member_emails
                else:
                    print(f"Error while getting the members of group {group_name}.")
                    print("Debug: API response while obtaining group members:")
                    print(members_response.text)
            else:
                print(f"Group {group_name} not found.")
        else:
            print(f"Error while getting group {group_name}.")
            print("Debug: API response while getting group:")
            print(response.text)

        return None

        return None

