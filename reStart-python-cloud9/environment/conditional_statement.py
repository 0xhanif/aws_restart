"""
Your module description
"""
#conditional statement
number=int(input("Enter the number: "))
if(number>0):
    print("{} is a positive number".format(number))
elif(number<0):
    print("{} is a negative number".format(number))
else:
    print("{} is zero".format(number))