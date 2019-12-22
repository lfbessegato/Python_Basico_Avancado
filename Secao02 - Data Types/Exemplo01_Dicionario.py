person = {
    "first_name" : "John",
    "last_name" : "Green",
    "birth_year": 1980,
    "country_of_birth": "Canada"
}
print(type(person))
print(person["first_name"])

person["birth_year"] = 1979
print(person)

person["marital_status"] = "Married"
print(person)

person["children"] = ["Nathalie", "Ethan"]
print(person)

person["children"].append("Ana")
print(person)

print(person.get("age", "invalid property"))
print(person.get("children", "invalid property"))

key = "first_name"
print(person[key])

person.clear()
print(person)