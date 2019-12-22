print('Data Type - Listas e Tuplas')
print('############ LISTAS ##############')
students = ["John", "Mary", "Steve"]
print(type(students))
print(len(students))
print(students[0])
print(students[-1])
print(students[:2])
print('########## TUPLAS ################')
months = ("January", "February", "March")
print(type(months))
print(months[0])
print(students)
students[0]="George"
print(students)

# Insere na ultima posicao
students.append("Kate")
print(students)

# Insere na posicao desejada
students.insert(0, "Peter")
print(students)

# remove o ultimo elemento
students.pop()
print(students)

# remove de uma posicao especifica
students.pop(1)
print(students)

# remove um elemento especifico
students.remove("Mary")
print(students)