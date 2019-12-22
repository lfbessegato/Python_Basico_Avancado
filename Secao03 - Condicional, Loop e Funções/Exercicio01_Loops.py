import random
people = []

for x in range(0,8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0,7)
random_person = people[index]

print("Picking a random person: ", random_person)