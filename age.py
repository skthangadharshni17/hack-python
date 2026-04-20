a=input("Enter the age:")
try:
   if a<0:
      raise RuntimeError
except RuntimeError:
   print("The age will not be negative.")
else:
   print("The age is positive.")
finally:
   print("End of the program")