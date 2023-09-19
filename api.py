import requests
import json 
url = "https://rapidapi.com/apidojo/api/realtor/"
response = requests.get(url)
print(response.text)
json.loads(response.content)
# print(response.status)
# print(response.content)