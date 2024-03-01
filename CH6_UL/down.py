import requests
response = requests.get('https://bit.ly/fruits_300_data')
with open('./data', 'wb') as f:
    f.write(response.content)