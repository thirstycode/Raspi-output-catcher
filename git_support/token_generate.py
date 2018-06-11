import time
import re
import random
import string
# time.sleep(60)
def new_token():
	random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

	from robobrowser import RoboBrowser
	browser = RoboBrowser()
	login_url = 'my_url'
	browser.open('https://github.com/login')
	form = browser.get_form()
	# print(form)
	form["login"].value = "thirstycode" 
	form["password"].value = ""
	# print(form)
	browser.submit_form(form)
	browser.open('https://github.com/settings/tokens/new')
	form = browser.get_forms()
	# print(form)
	form[3]["oauth_access[description]"].value = random_string
	form[3]["oauth_access[scopes][]"].value = ['repo', 'admin:org',  'admin:public_key',  'admin:repo_hook',  'admin:org_hook', 'gist', 'notifications', 'user',  'delete_repo', 'write:discussion',  'admin:gpg_key']
	browser.submit_form(form[3])

	# print(browser.parsed())
	src = str(browser.parsed())

	start = '<code class="token" id="new-oauth-token">'
	end = '</code>'

	result = re.search('%s(.*)%s' % (start, end), src).group(1)
	return(result)
	print(result)