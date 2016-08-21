import requests
import datetime

response = requests.post('http://challenge.code2040.org/api/dating',
data = {'token':'38435f83ebfecb02e00892e83c22862f'})

contents = response.json()
seconds, date = contents['interval'], contents['datestamp']

date_time_seperated = date.split('T')

date = date_time_seperated[0].split('-')
time = date_time_seperated[1].split(':')

time[2] = time[2][:len(time[2])-1]

days = seconds // (3600*24)
seconds_left = seconds % (3600*24)

new_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]),
int(time[0]), int(time[1]), int(time[2]))
time_elpased = datetime.timedelta(days, seconds_left)
new_date = new_date + time_elpased
result = new_date.isoformat() + 'Z'

requests.post('http://challenge.code2040.org/api/dating/validate',
data = {'token':'38435f83ebfecb02e00892e83c22862f', 'datestamp': result})
