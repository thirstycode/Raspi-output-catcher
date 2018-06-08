import time
from git import push_to_github

# time.sleep(300)

token = ""
filename="README.md"
repo = "thirstycode/Raspi-output-catcher"


while True:
	push_to_github(filename, repo, "master", token)
	time.sleep(300)
