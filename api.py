import requests

API_ENDPOINT = "https://sef.podkolzin.consulting/api/users/lastSeen?offset={}"

def fetch_all_users_data():
    offset = 0
    all_users = []

    while True:
        response = requests.get(API_ENDPOINT.format(offset))
        if response.status_code != 200:
            raise Exception(f"API returned {response.status_code}: {response.text}")
        data = response.json()
        if not data.get('data'):
            break
        all_users.extend(data.get('data'))
        offset += len(data.get('data'))


    return all_users
