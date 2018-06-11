import time
from git_support.git import push_to_github
from git_support.token_func import open_token

# time.sleep(300)

token = open_token()
filename="README.md"
repo = "thirstycode/Raspi-output-catcher"


while True:
	push_to_github(filename, repo, "master", token)
	time.sleep(300)