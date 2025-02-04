import pyeapi


# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista1vt9'

node = pyeapi.connect(host='leaf1',username=USERNAME, password=PASSWORD, return_node=True)

response = node.enable('show version',encoding='json')

print(response)

