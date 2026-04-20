#program handling program and display number
try:
   user_input =int(input("Enter a number: "))
   number = int(user_input)
   print("You entered:",number)
except ValueError as e:
   print("Invalid input. Please enter a valid number.")
