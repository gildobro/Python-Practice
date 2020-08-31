myfile = open("files/fruits.txt")
content = myfile.read()
myfile.close()

with open("files/fruits.txt") as myfile:
    content = myfile.read()


print(content)