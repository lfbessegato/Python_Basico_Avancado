import requests
import json
import pprint

r = requests.get("https://opentdb.com/api.php?amount=1&category=12&diffculty=easy&type=multiple")
print(r.status_code)

print(r.text)
print(type(r.text))

question = json.loads(r.text)
print(question)
print(type(question))

pprint.pprint((question))
print(question['results'][0]['category'])
print(question['results'][0]['incorrect_answers'])

person = {'Name': 'John', 'Age': 30}
person_json = json.dumps(person)
print(person_json)
print(type(person_json))