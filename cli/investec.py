import json
import base64
import os
import requests
from tabulate import tabulate

class Investec:
    def __init__(self, credentials_path='~/.investecli/credentials'):
        credentials = json.load(open(os.path.expanduser(credentials_path)))

        self.credentials_path = credentials_path
        self.client_id = credentials.get('client_id', None)
        self.client_secret = credentials.get('client_secret', None)
        self.token = credentials.get('token', None)
        self.token_type = credentials.get('token_type', None)

    def login(self):
        response = requests.post(
            'https://openapi.investec.com/identity/v2/oauth2/token',
            auth=(self.client_id, self.client_secret),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data={
                'grant_type': 'client_credentials',
                'scope': 'accounts'
            })

        data = response.json()

        self.token = data['access_token']
        self.token_type = data['token_type']

        json.dump({
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'token': self.token,
            'token_type': self.token_type,
        }, open(os.path.expanduser(self.credentials_path), 'w+'))


    def accounts(self):
        response = requests.get(
            'https://openapi.investec.com/za/pb/v1/accounts',
            headers={'Authorization': f'{self.token_type} {self.token}'})

        data = response.json().get('data', None)

        print(tabulate(data['accounts'], headers='keys', tablefmt='presto'))


    def balance(self, account_id):
        response = requests.get(
            f'https://openapi.investec.com/za/pb/v1/accounts/{account_id}/balance',
            headers={'Authorization': f'{self.token_type} {self.token}'})

        data = response.json().get('data', None)
        print(tabulate([data], headers='keys', tablefmt='presto'))


    def transactions(self, account_id):
        response = requests.get(
            f'https://openapi.investec.com/za/pb/v1/accounts/{account_id}/transactions',
            headers={'Authorization': f'{self.token_type} {self.token}'})

        data = response.json().get('data', None)

        print(tabulate(data['transactions'], headers='keys', tablefmt='presto'))
