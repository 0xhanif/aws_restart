"""
Your module description
"""
import json

mylist=[10,"hello",True,9.8]
print(mylist,type(mylist))
mystr=json.dumps(mylist)
print(mystr,type(mystr))

newlist=json.loads(mystr)
print(newlist,type(newlist))

mydict={"name":"John","age":"40","designation":"cloud enginner"}
print(type(mydict),mydict)
mystr=json.dumps(mydict)
print(type(mystr),mystr)

newobject=json.loads(mystr)
print(type(newobject),newobject)