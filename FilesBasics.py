'''
#read from an existing file
with open("files/fruits.txt", "r") as myfile:
    content = myfile.read()

print(content)

#write to a non-existing file
with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Pepper\nCucumber\nOnion\nTomato")
    myfile.write("\nGarlic")
'''

#append content to the end of a file and '+' for reading
with open("files/vegetables.txt", "a+") as myfile:
    myfile.write("\nEggplant")
    #the seek method moves the cursor to point 0
    myfile.seek(0)
    content = myfile.read()

print(content)