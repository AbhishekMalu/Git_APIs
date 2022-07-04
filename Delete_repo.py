import requests
import json
#To Access the Token of github
with open("token.json",'r') as data:
    config_file = data.read()
token = json.loads(config_file)

user = "abhiumesh"
repo = "Git_API"

path = f"repos/{user}/{repo}"
url = f"https://api.github.com/{path}"


header = {
    "Authorization" : f"token {token['token']}"
}

response = requests.delete(url,headers=header)
print(response.status_code)