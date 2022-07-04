import requests
import json
import pandas as pd

user_name = "abhiumesh"
path = "users/{}".format(user_name)
url = f"https://api.github.com/{path}/repos"

response = requests.get(url).json()

column = ["Repo_name","user_photo_url","Repo_url","Created_Time"]
User_detail = []
for repo_detial in response:
    User_detail.append([repo_detial["full_name"],repo_detial['owner']["avatar_url"],repo_detial["html_url"],repo_detial["created_at"]])


frame = pd.DataFrame(User_detail,columns=column)
print(frame)


