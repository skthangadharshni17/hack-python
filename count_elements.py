def count_elements(string):
   digits=spaces=alphabets=0
   for char in string:
      if char.isdigit():
       digits+=1
      elif char.isspace():
       spaces+=1
      elif char.isalpha():
       alphabets+=1
   print("No.of digits:",digits)
   print("No.of characters:",alphabets)
   print("No.of spaces:",spaces)
#main routine
strings=input("Enter a string:")
count_elements(strings)