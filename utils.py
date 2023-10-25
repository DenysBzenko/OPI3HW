import requests
from datetime import datetime

def get_last_seen_online(offset):
    # Replace with your actual API endpoint and offset
    url = f"https://sef.podkolzin.consulting/api/users/lastSeen?offset={offset}"

    try:
        response = requests.get(url)

        # Log the status code and response text
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")

        response.raise_for_status()  # Raises a HTTPError if the response status is 4xx, 5xx

        data = response.json()
        # Check if 'lastSeen' field is in the response and it's not None
        if 'lastSeen' in data and data['lastSeen'] is not None:
            last_seen_timestamp = data['lastSeen']
            # Convert the timestamp to a human-readable format
            last_seen_date = datetime.fromtimestamp(last_seen_timestamp)
            return last_seen_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            print("Unexpected response structure or no data available.")
            return None

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except ValueError as e:  # Includes JSON decoding errors
        print(f"Error decoding the response: {e}")
        return None
    except Exception as e:  # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")
        return None
