class MyClass:
    def __init__(self, x):
        self.x = int(x)

    def check(self):
        self.a = int(input("enter the first angle: "))
        self.b = int(input("enter the second angle: "))
        self.c = int(input("enter the third angle: "))
        if ((self.a + self.b + self.c) == self.x) and (self.a > 0) and (self.b > 0) and (self.c > 0):
            print("these angles could belong to a triangle!")
        else :
            print("these angles couldn't belong to a triangle!")

tr = MyClass(180)
tr.check()