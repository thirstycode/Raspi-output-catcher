import base64
import requests
import json
from git_support.token_generate import new_token
from git_support.token_func import save_token

def push_to_github(filename, repo, branch, token):
    url="https://api.github.com/repos/"+repo+"/contents/"+filename

    base64content=base64.b64encode(open(filename,"rb").read())

    data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
    try:
        if data['message'] :
            token = new_token()
        save_token(token)
        data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
    except:
        # print("Token sahi")
        pass
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
