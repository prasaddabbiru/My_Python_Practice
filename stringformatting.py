age = 24
#print(" My age is " + age + " years") --- Throws an error since "age" is not a string its an integer
print(" My age is " + str(age) + " years")
print(" My age is {0} years".format(age))
print(" There are {0} days in {1},{3},{5},{7},{8},{10},{12} & {13} days in {4},{6},{9},{11} & only {14} days in {2} ".format(31,"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec",30,28))

print("""Jan : {2}  days
Feb : {0} days
Mar : {2} days
Apr : {1} days
May : {2} days
Jun : {1} days
Jul : {2} days
Aug : {2} days
Sep : {1} days
Oct : {2} days
Nov : {1} days
Dec : {2} days\n""".format(28,30,31) )

print("My age is %d years" %age)
print("My age is %d %s %d %s \n" %(age,"years",6,"months"))

for i in range(1, 12):
    print("No.%2d squared is %4d and cubed is %4d" %(i, i**2 , i**3 ))
print("Pi is approximately %12.50f" %(22/7))
