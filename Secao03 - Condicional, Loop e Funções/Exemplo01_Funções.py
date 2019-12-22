def say_hello():
    print("Hello!")

def say_hello_arguments(person1, person2):
    print("Hello " + person1 + ", how are you doing? " + person2 + " is waiting for you.")

def fahrTocelsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

say_hello()
person1 = "Marcia"
person2 = "Luciano"
say_hello_arguments(person1, person2)

print("Celsius: ", round(fahrTocelsius(100),2))
print("Kelvin: ", round(fahrTocelsius(100) + 273.5 ,2) )