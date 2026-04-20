import math
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
lcm=(num1*num2)//math.gcd(num1,num2)
print("The LCM is ",lcm)