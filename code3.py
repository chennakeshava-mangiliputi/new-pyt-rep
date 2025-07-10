def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by zero is undefined")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print(divide(a,b))