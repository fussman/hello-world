import requests

url = "http://192.168.10.80/restconf/api/config/native/interface/Loopback/500"

payload = "{\n  \"ned:Loopback\": {\n    \"name\": 500,\n    \"ip\": {\n      \"address\": {\n        \"primary\": {\n          \"address\": \"170.99.1.1\",\n          \"mask\": \"255.255.255.0\"\n        }\n      }\n    }\n  }\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
