"""
Your module description
"""
try:
	fp=open("file4",'r')
	fp.read()
	fp.close()
except:
	print("there is no file 4")