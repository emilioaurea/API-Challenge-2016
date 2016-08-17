# Open source Python library for HTTP
import requests

register = requests.post('http://challenge.code2040.org/api/register',
data = {'token': '38435f83ebfecb02e00892e83c22862f',
        'github': 'https://github.com/emilioaurea/API-Challenge-2016.git'})
