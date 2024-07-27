try:
    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))
    if a>b:
        print("First is greater")
    elif a==b:
        print("Both are equal")
    else:
        print("Second is greater")
except valueError:
    print("Invalid input")