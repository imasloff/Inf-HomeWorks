class MyClass:
    def __init__(self, x):
        self.x = int(x)

    def check(self, a, b, c):
        if a + b + c == self.x :
            print("sum = " + str(self.x))
        else :
            print("sum != " + str(self.x))

ob1 = MyClass(90)
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
ob1.check(a, b, c)
