"""
Your module description
"""
f1=open("file1",'r')
data=f1.read()
f2=open("file2",'a')
f2.write(data)
f1.close()
f2.close()
