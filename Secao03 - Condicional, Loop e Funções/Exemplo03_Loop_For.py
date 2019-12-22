blog_posts = ["","The 10 coolest math functions in Python","",
              "How to make HTTP requests in Python",
              "A tutorial about data types in Python"]
for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print("---------------------")
myString = "This is a String"
for char in myString:
    print(char)

print("---------------------")
for x in range(0,10):
    print(x)

print("---------------------")
person = {'Name' : 'Karen Smith', 'Age' : 25, 'Gender' : 'Female'}
for key in person:
    print(key, ":", person[key])

print("---------------------")
blog_posts = {"Python" : ["The 10 coolest math functions in Python",
              "How to make HTTP requests in Python",
              "A tutorial about data types in Python"],
              "JavaScript" : ["Namespaces in Javascript", "New functions available in ES6"]}
for category in blog_posts:
    print("Posts about", category)
    for post in blog_posts[category]:
        print(post)
