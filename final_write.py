# from git import push_to_github
from write import write_md
from datetime import datetime as dt

def final_write(message):
	t= dt.now()
	out_time = t.strftime('%I:%M:%S %p %d %m')
	write_md(out_time + " --> " + message)
