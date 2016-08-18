import requests

response = requests.post('http://challenge.code2040.org/api/haystack',
data = {'token': '38435f83ebfecb02e00892e83c22862f'})

content = response.json()
haystack, needle = content['haystack'], content['needle']
index = haystack.index(needle)

requests.post('http://challenge.code2040.org/api/haystack/validate',
data = {'token': '38435f83ebfecb02e00892e83c22862f',
        'needle': index})
