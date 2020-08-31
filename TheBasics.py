#non-keyword/non positional arguments
def area(a, b):
    return a * b

print(area(4,5))

#Positional arguments/ keyword arguments
#The position doesn't matter but a value is 
# assigned to each parameter
print(area(b=4, a=5))


#A default parameter is when the keyword is 'a=' is assigned to
#an argument at the beginning of the function
#an Important note is that a non-default argument can only go AFTer
#a default argument and NOT before