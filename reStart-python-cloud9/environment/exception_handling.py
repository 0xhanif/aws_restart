"""
Your module description
"""
divisor=int(input("enter the divisor: "))
dividend=int(input("enter the dividend: "))
try:
	print(dividend/divisor)
except:
	print("invalid input for divisor. provide value other than zero")

print("end of the program")