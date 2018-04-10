name = str(input("Enter your name : "))
age = int(input("hi how are you  {0} ?".format(name)))

if 18<=age<=31:
    print(" {} , ".format(name))
elif age<18:
    print("{}".format(18-age))
else: print("{} ". format(name))

