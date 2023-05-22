# Importar la clase JumpcloudDirector
from utils.service import JumpcloudDirector
from utils.credentials import *

# Create an instance with your API Key
api_key = api_key
director = JumpcloudDirector(api_key)
group_id = "<YOUR GROUP ID>"

member_emails = director.get_group_members_emails("Access_Github")

if member_emails:
    print(f"The emails of the group members {group_id} are: {member_emails}")
else:
    print(f"Not possible to retreive group members from group {group_id}.")