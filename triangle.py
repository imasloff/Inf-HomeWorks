a=int(input("enter angle a (deg): "))
b=int(input("enter angle b (deg): "))
c=int(input("enter angle c (deg): "))

if ((a + b + c) == 180) and (a > 0) and (b > 0) and (c > 0):
    print("these angles could belong to a triangle!")
else:
    print("these angles couldn't belong to a triangle!")