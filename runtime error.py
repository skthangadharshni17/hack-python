r=input("Enter the radius:")
try:
   if r<0:
      raise RuntimeError
except RuntimeError:
   print("The radius will not be negative.")
else:
   print("The radius is positive.")
finally:
   print("End of program")