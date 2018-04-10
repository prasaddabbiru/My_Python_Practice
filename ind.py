#Print the index number of the item from the list
a=[23, 12, 42, 32, 55, 23, 12, 42, 32, 55, 23, 12, 42, 32, 55]
x = int(input("Enter the number to search index : "))
for i in range(0,len(a)):
    if(a[i]==x):
        print(a.index(x,i))

##if x in a:
##    for i in range(len(a)):
##        if(x==a[i]):
##            print(x, i)
    

