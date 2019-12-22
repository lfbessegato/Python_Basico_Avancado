import requests

r = requests.get(("https://www.google.com"))
print(r.status_code)

# Status - Code
# 200 - OK
# 403 - forbidden
# 404 - Not Found

print(r.headers)
print(r.headers["Date"])
print(r.text)