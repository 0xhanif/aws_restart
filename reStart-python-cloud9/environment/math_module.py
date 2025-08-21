"""
Your module description
"""
import math

def area_of_circle(radius):
	area=math.pi*math.pow(radius,2)
	return area

def circumference_of_circle(radius):
	circumference=2*math.pi*radius
	return circumference

print("area of the circle is: ",area_of_circle(7))
print("circumference of the circle: ",circumference_of_circle(7))