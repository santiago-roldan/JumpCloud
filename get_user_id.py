from utils.service import JumpcloudDirector
from utils.credentials import *

# Create a Jumpcloud instance with your API Key
api_key = api_key
director = JumpcloudDirector(api_key)

# insert user's email
email = "<USER'S EMAIL>"

# Call method get_user_id to obtain user's ID
user_id = director.get_user_id_by_email(email)

# Check if the user's ID is correct
if user_id is not None:
    print(f"The ID of the user '{email}' is: {user_id}")
else:
    print(f"User with the email '{email}' not found.")
