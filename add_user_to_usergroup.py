# Importar la clase JumpcloudDirector
from utils.service import JumpcloudDirector
from utils.credentials import *


api_key = api_key
director = JumpcloudDirector(api_key)
user_id = input("Please, insert the users's ID: ")
group_id = "<GROUP ID>"
director.add_user_to_group(user_id, group_id)





