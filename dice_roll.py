import random
x=random.randrange(1,7)
print(x)
z = input("Enter y or Y to continue: ")
z.lower()
while z == 'y':
    x=random.randrange(1,7)
    print(x)
    z = input("Enter y or Y to continue: ")
    z.lower()
