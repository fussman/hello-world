import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-cookie" : "o4lKNXBZdZtpAkLsqHUJR6TyB3KqlqhbJP4ItoWr6x3HUG99H1tBsH1TmE5rC1PpBaIVmf550I4rIOqDyOU+PYBYieIZETQxH0ZNCz/infO9hZ0KwUA5RRU87t4E3Ri3zlHqjwLXyT0CNh/Q43epMuKlr9VQdDLGilx1zrCcELo="}
headers = {'Authorization': 'Basic Og=='}

response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)