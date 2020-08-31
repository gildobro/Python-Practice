'''
#the len() method outputs the amount of characters that a string has
#can only take one argument
print(len('stefonapodopoulous'))
#len = 18

#the isinstance() method checks if an argument is an instance of another argument
#must have 2 arguments. no more, no less.
#Example
print(isinstance(11,int))
print(isinstance(13, float))
print(isinstance("hello", str))
print(isinstance(1,3,int))
#output1 = True
#output2 = False
#output3 = True
#output4 = TypeError: isinstance expected 2 arguments, got 3

#non-keyword arguments
def mean(*args):
    print(len(args))
    return sum(args) / len(args)
print(mean(1,3, 7, 5.3, 12))

#keyword arguments
def mean(**kwargs):
    return kwargs

print(mean(a=1,b=2,c=3))
'''