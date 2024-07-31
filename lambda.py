def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
mytripler=myfunc(3)
print(mydoubler(5))
print(mytripler(7))

my=["apple","banana","cherry"]
print(my[-1])