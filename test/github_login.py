#!/usr/bin/python3
import requests
import uuid
r = requests.get('https://api.github.com/user', auth=('luxianyou', 'SSYyly@5201314'))
print(r.status_code)
print(r.json())

uuid_str = str(uuid.uuid1())

print(uuid_str.replace('-',''))
