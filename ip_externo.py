import requests
import json

r = requests.get('http://ifconfig.co/json')

if r.status_code == 200:
    print('Successo!')
elif r.status_code == 404:
    print('Página não encontrada ou sem conexão de internet.')


dic = json.loads(r.text)
ip = dic['ip']
teste = dic['user_agent']['version']
print(f'{ip }')
print(f'{teste}')
