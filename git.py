import base64
import requests
import json

def push_to_github(filename, repo, branch, token):
    url="https://api.github.com/repos/"+repo+"/contents/"+filename

    base64content=base64.b64encode(open(filename,"rb").read())

    data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
    # print(data)
    sha = data['sha']

    # print(base64content.decode('utf-8'))
    # print(data['content'].replace("\n",""))

    if base64content.decode('utf-8') != data['content'].replace("\n",""):
        message = json.dumps({"message":"update",
                            "branch": branch,
                            "content": base64content.decode("utf-8") ,
                            "sha": sha
                            })

        resp=requests.put(url, data = message, headers = {"Content-Type": "application/json", "Authorization": "token "+token})

        # print(resp)
        print("Successfull")
    else:
        print("nothing to update")
