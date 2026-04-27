def count_case(s):
   lowercase=sum(1 for char in s if char.islower())
   uppercase=sum(1 for char in s if char.isupper())
   return(lowercase,uppercase)
#main routine
str=input("Enter a string:")
lower,upper=count_case(str)
print("Uppercase letters:",upper)
print("Lowercase leters:",lower)