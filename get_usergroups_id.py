import http.client
import json

conn = http.client.HTTPSConnection("console.jumpcloud.com")

payload = ""

headers = {
    'x-api-key': "<YOUR API KEY>",
    'x-org-id': "<YOUR ORG ID>"
}

conn.request("GET", "/api/v2/groups?limit=500&skip=0", payload, headers)

res = conn.getresponse()
data = res.read()

groups = json.loads(data.decode("utf-8"))

usergroups = []
for group in groups:
    if group['type'] == 'user':
        usergroup = {
            'id': group['_id'],
            'name': group['name']
        }
        usergroups.append(usergroup)

for usergroup in usergroups:
    print(usergroup)
