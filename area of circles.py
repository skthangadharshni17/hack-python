import math
def area_circle(r):
   area=math.pi*(math.pow(r,2))
   return area
r=int(input("Enter the radius:"))
area_of_circle=area_circle(r)
print("The area of the circle:",area_of_circle)