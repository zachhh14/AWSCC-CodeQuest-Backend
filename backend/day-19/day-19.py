import requests
from datetime import datetime

# API endpoint (example using JSONPlaceholder API)
api_url = "https://api.spacexdata.com/v5/launches/latest"

# Sending a GET request
response = requests.get(api_url)

def getCrewName(id):
    response = requests.get(f"https://api.spacexdata.com/v4/crew/{id}")
    data = response.json()
    return data['name']

def getLaunchName(id):
    response = requests.get(f"https://api.spacexdata.com/v4/launchpads/{id}")
    data = response.json()

    return f"{data['name']} ({data['full_name']})"

# Handling the response
if response.status_code == 200:
    # Response content as JSON
    data = response.json()

    print('Launch name: ',data['name'])
    print('Launchpad name: ',getLaunchName(data['launchpad']))
    converted_date = datetime.fromisoformat(data['date_utc'][:-1])
    formatted_date = converted_date.strftime("%m/%d/%Y")
    formatted_time = converted_date.strftime("%H:%M:%S")
    print(f'Schedule: {formatted_date} {formatted_time}')
    print('\nCrews that are involved:')
    for crew_member in data['crew']:
        print('- ',getCrewName(crew_member['crew']))
    
    print(f"\nResources: {data['links']['reddit']['launch']}")
else:
    print(f"Request failed with status code: {response.status_code}")