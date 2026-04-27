def reverse_string(s):
   return s[::-1]
def is_palindrome(s):
   return s==reverse_string(s)
#main routine
str=input("Enter a string:")
reversed_string=reverse_string(str)
if is_palindrome(str):
   print("Reversed string:",reversed_string)
   print("The string is palindrome.")
else:
   print("Reversed string:",reversed_string)
   print("The string is not palindrome.")