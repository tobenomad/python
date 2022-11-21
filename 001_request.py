import requests

url = "http://www.python.org"

resp = requests.get(url, verify=False)

print(resp)
