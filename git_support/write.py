def write_md(string):
	with open("README.md","r") as thefile:
		content = thefile.readlines()
	content.insert(2,"-	" + string + "\n")
	with open("README.md","w") as thefile:
		for item in content:
			thefile.write("%s" % item)