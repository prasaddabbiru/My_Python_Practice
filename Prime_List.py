a=[]
x= int(input("Enter range to list prime numbers:"))
for number in range(2,x+1):
    a.append(number)
    
    for i in list(a):
        if((i//number)==1):
            print(i)
        i+=1


           
