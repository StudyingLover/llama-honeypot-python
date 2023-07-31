import requests

url = 'http://localhost:8000/v1/chat/completions'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    'messages': [
        {
            'content': 'You are a helpful assistant.',
            'role': 'system'
        },
        {
            'content': 'What is the capital of France?',
            'role': 'user'
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())