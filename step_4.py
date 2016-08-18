import requests

response = requests.post('http://challenge.code2040.org/api/prefix',
data = {'token': '38435f83ebfecb02e00892e83c22862f'})

content = response.json()
prefix, words = content['prefix'], content['array']
prefix_size = len(prefix)
words_without_prefix = [word for word in words if not word[:prefix_size] == prefix]

r = requests.post('http://challenge.code2040.org/api/prefix/validate',
data = {'token': '38435f83ebfecb02e00892e83c22862f',
        'array': words_without_prefix})
print(words)
print(prefix)
print(words_without_prefix)
print(r.text)
