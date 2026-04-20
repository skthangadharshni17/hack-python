
try:
   n=int(input("Enter numerator:"))
   d=int(input("Enter denominator:"))
   if d==0:
      raise ZeroDivisionError("Denominator can't br zero.")
   result=n/d
   print("Result:",result)
except ZeroDivisionError as e:
   print("Error:",e)