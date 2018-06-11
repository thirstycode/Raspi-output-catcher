

def save_token(token):
	with open('token.txt','w+') as token_file:
		token_file.write(token)

def open_token():
	with open('token.txt','r') as token_file:
		token = token_file.read()
	return token