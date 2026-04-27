def add_five():
   numbers=input("Enter five numbers separated by spaces:").split()
   numbers=[int(num)for num in numbers]
   updated_num=[num+5 for num in numbers]
   print("Updates List:",updated_num)
add_five()