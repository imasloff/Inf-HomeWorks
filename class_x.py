class MyClass:
    def __init__(self, x):
        self.x = int(x)

    def check(self):
        self.a = int(input("enter the first number: "))
        self.b = int(input("enter the second number: "))
        self.c = int(input("enter the third number: "))
        if (self.a + self.b + self.c) == self.x :
            print("sum = " + str(self.x))
        else :
            print("sum != " + str(self.x))

ob1 = MyClass(90)
ob1.check()