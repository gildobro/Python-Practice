def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        return "\nZero Division is Undefined!!"

userNum1 = int(input("Please enter first number: "))
userNum2 = int(input("Please enter second number: "))

print(divide(userNum1,userNum2))