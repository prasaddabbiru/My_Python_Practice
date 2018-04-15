k = []
x = int(input("Enter range: "))
<<<<<<< HEAD
if(x>0):
    for i in range(x):
        y= int(input("enter value: "))  
        k.insert(i,y)       
for j in list(k):
    if k.count(j)>1:
        k.remove(j)
print(sorted(k))
=======
if(x>=0):
    for i in range(x):
        y= int(input("enter value: "))  
        k.insert(i,y)
        
for j in list(k):
    if k.count(j)>1:
        k.remove(j)
print(k.sort())
>>>>>>> 7e7f6bde4dc4981ad067aa151534c3bd77438621

