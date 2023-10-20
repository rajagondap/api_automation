import json

import requests

r = requests.get("https://api.nasa.gov/planetary/apod", params = {"api_key": "q4SF3jUHnzqUUAT1KIOmyV8gJrFG2HtfBVNgJigW"})
print(r.status_code)
print(r.url)



