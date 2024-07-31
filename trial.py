class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printname(abc):
        print(abc.fname,abc.lname)
class Student(Person):
    def __init__(self, fname, lname, gyear):
        super().__init__(fname, lname)
        self.graduationyear=gyear
    def func(self):
        return f"Hello, {self.lname},{self.fname} graduation on {self.graduationyear}"
x=Student("John","Doe",2019)
x.func()