import requests

response = requests.post('http://challenge.code2040.org/api/reverse',
data = {'token': '38435f83ebfecb02e00892e83c22862f'})

reversed_response = response.text[::-1]

requests.post('http://challenge.code2040.org/api/reverse/validate',
data = {'token': '38435f83ebfecb02e00892e83c22862f',
        'string': reversed_response})
