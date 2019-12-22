months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

birthday = input("Type your birthday in the format DD-MM-YYYY: ")
index = int(birthday[3:5]) - 1
bd_month = months[index]

print("You were born in", bd_month)

