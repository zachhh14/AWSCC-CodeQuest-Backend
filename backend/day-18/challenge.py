import requests

# Base API URL
base_url = 'https://jsonplaceholder.typicode.com/posts'

headers = {
    "'User-Agent": 'MyApp/1.0',
}


# Adding query parameters to the URL
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    response_data = response.json()

    for data in response_data:
        print(data)
else:
    print(f'API request failed, status code: {response.status_code}')

post_url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'masaya',
    'body': 'joke lang'
}

post_response = requests.post(post_url, json=data)

if post_response.status_code == 201:
    print(f'post reponse: {post_response.status_code}')
    print('success post')



