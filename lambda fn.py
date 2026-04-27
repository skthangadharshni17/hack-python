def square():
   nums=input("Enter the numbers:").split()
   nums=[int(num)for num in nums]
   squared_num=[(lambda x:x**2)(x)for x in nums]
   return squared_num
result=square()
print("Squared elements:",result)