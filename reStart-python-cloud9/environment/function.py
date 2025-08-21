"""
Your module description
"""
#definition
def addition(a,b):
    print(a+b)
#calling
addition(10,20)
addition(12,34)

#no argument and no return
def myfun():
    a=int(input("Enter the first value: "))
    b=int(input("Enter the second value: "))
    print("Sum is: ",a+b)
    
myfun()

#with argument and no return
def myfun2(a,b):
    print("Sum is: ",a+b)

myfun2(10,80)

#with argument and with return
def myfun3(a,b):
    return a+b
    
print(myfun3(20,80))

#no argument and with return
def myfun4():
    return "hello"
    
print(myfun4())