# Importar la clase JumpcloudDirector
from utils.service import JumpcloudDirector
from utils.credentials import *

# Create a Jumpcloud instance with your API key
api_key = api_key
director = JumpcloudDirector(api_key)

# Fill the with the user's data
first_name = input("Please insert user's name: ")
last_name = input("Please insert user's lastname: ")
password = '<SUPER SECURE PASSWORD>'

# Generate username with "name.lastname"
username = f"{first_name.lower()}.{last_name.lower()}"

# Call method create_user to create a user
user_data = director.create_user(first_name, last_name, username, password)

# Check if the user was created successfully
if user_data is not None:
    print("User created successfully:")
    print(user_data)
else:
    print("Error while creating the user.")
