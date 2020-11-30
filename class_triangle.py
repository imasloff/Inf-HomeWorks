class MyClass:
    def __init__(self, x):
        self.x = int(x)

    def check(self, a, b, c):
        if (self.x == a + b + c) and (a > 0) and (b > 0) and (c > 0):
            print("these angles could belong to a triangle!")
        else :
            print("these angles couldn't belong to a triangle!")

tr = MyClass(180)
a = int(input("enter the first angle: "))
b = int(input("enter the second angle: "))
c = int(input("enter the third angle: "))
tr.check(a, b, c)
