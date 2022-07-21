import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = 'h3hhdhhehhdssjlJJ'
USERNAME = 'gen2proff'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    'id': 'graph20',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'int',
    'color': 'ajisai',
}
header = {
    "X-USER-TOKEN": TOKEN,
}
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
today = datetime.now()
print(today.strftime('%Y%m%d'))

cycling_param = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '15',
}
pixel_creation_endpoint = f'{graph_endpoint}/graph20'
response = requests.post(url=pixel_creation_endpoint, json=cycling_param, headers=header)
print(response.text)
