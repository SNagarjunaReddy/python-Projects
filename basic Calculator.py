print("""
1. Addition
2. Subtraction
3. division
4. multiplication
5. Exponent
6. square root
0. Exit

""")
operation = int(input("select your operation : "))
if operation == 1:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1+number2)
elif operation == 2:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1-number2)
elif operation == 3:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1/number2)
elif operation == 4:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1*number2)
elif operation == 5:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1**2)
elif operation == 6:
    number1=int(input("enter your first number :"))
    number2=int(input("enter your second number : "))
    print("answer", number1**0.5)
elif operation == 0:
    print("exiting the application")
else:
    print("invalid selected operation")
