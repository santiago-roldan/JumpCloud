import http.client

conn = http.client.HTTPSConnection("console.jumpcloud.com")

payload = ""

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'x-api-key': "API_KEY"
    }

conn.request("GET", "/api/systemusers", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
