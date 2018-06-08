from git import push_to_github
from write import write_md
from datetime import datetime as dt

token = "c54480e5ce0c442dfc37d110b79e31a9807a6a4a"
filename="README.md"
repo = "thirstycode/Raspi-output-catcher"


def final_push(message):
	t= dt.now()
	out_time = t.strftime('%I:%M:%S %p %d %m')
	write_md(out_time + " --> " + message)
	push_to_github(filename, repo, "master", token)

final_push("new")
