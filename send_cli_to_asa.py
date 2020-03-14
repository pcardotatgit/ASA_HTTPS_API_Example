import requests
from pprint import pprint
'''
	read the cli_commands.cfg file and send cli commands to ASA, create new service objects
	this script uses ASA https APIs ( not REST APIs )
	
	RQ : ISSUE with le slash de : Interface GigabitEthernet0/2.20
'''

# Change information here under
username="admin"
password="cisco123"
server="https://192.168.200.10"

input(' Let s execute a show version first just to check if the ASA is alive. Type Enter ' )
api_auth_path = "/admin/exec/show version"
auth_url = server + api_auth_path
r = requests.get(auth_url, auth=(username,password), verify=False)
pprint(r.text)
input(' If Connexion to ASA is Ok . type Enter ' )

line_content = []
with open('cli_commands.cfg') as inputfile:
	for line in inputfile:
		if line[0] == "#":
			pass
		else:
			line_content.append(line)

# loop through all content
command=""
for content in line_content:	
	print (content)		
	if content!="":
		if content[0]==" ":
			command_to_send=command+"/"+content
			api_auth_path = "/admin/exec/conf+t/"+command_to_send
			print (api_auth_path)
			auth_url = server + api_auth_path
			r = requests.get(auth_url, auth=(username,password), verify=False)
			pprint(r.text)	
		else:
			command=content
			api_auth_path = "/admin/exec/conf+t/"+command
			print (api_auth_path)
			auth_url = server + api_auth_path
			r = requests.get(auth_url, auth=(username,password), verify=False)
			pprint(r.text)	
			command=command.replace("\r","")
			command=command.replace("\n","")

input(' Let s do a Write memory now')
api_auth_path = "/admin/exec/write mem"
auth_url = server + api_auth_path
r = requests.get(auth_url, auth=(username,password), verify=False)
pprint(r.text)
print ('============>  OK DONE !')
print()
print()



