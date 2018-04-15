x = int(input("Enter number:"))
even_numbers = []
odd_numbers = []
for number in range(0,x):
    if(number%2 == 0):
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Even Numbers between 0 to {} : ".format(x), even_numbers)
print("Odd Numbers between 0 to {} :  ".format(x), odd_numbers)

    
