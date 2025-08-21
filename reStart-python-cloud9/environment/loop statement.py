"""
Your module description
"""
#for loop statement
number=int(input("Enter the number : "))
fact=1
for i in range(1,number+1):
    fact=fact*i
print("Factorial of {} is {}".format(number,fact))

#while loop statement
number=int(input("Enter the number : "))
i=1
fact=1
while(i<=number):
    fact=fact*i
    i+=1
print(fact)