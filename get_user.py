import http.client

conn = http.client.HTTPSConnection("console.jumpcloud.com")

payload = ""

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'x-api-key': "API-KEY"
    }

conn.request("GET", "/api/systemusers/USERID", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))