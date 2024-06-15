# get_token.py
import requests
import base64
import sys

# Replace with your own Client ID and Client Secret
CLIENT_ID = 'bca28f1ae40248349d20dadb3c462a29'
CLIENT_SECRET = 'f2ede6c6fb384387a364f6ba2a0f2249'

def get_access_token():
    # Base64 encode the client ID and client secret
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    # Request the access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
        return access_token
    else:
        print("Error obtaining access token.")
        sys.exit()
