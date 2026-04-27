def swap(a,b):
   t=a
   a=b
   b=t
   return a,b

#main routine
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
x,y=swap(x,y)
print("After swapping:")
print("The 1st value is:",x)
print("The 2nd value is:",y)