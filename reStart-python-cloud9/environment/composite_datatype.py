"""
Your module description
"""
#composite data types
#list
mylist=[10,4.5,"hi",True,8+2j]
print(mylist,type(mylist))
print(len(mylist))
print(mylist[0],mylist[4],mylist[-2],mylist[1:4])
print(mylist[-5:-2])
print(mylist[1:4:2])
print(mylist[0::2])
print(mylist[:3])
print(mylist[1:])

mylist2=[19.4,300,False,"good morning"]
print(mylist2,type(mylist2))
print(mylist2[-3:-1])
mylist2[3]="good evening"
print("new list",mylist2)