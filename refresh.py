import time
from git import push_to_github

# time.sleep(300)

token = "c54480e5ce0c442dfc37d110b79e31a9807a6a4a"
filename="README.md"
repo = "thirstycode/Raspi-output-catcher"


while True:
	push_to_github(filename, repo, "master", token)
	time.sleep(300)