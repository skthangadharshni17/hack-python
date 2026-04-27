def second_largest(nums):
   if len(nums)<2:
      raise valueerror("List must contain atleast 2 numbers.")
   first,second=float('-inf'),float('-inf')
   for num in nums:
      if num>first:
       second,first=first,num
      elif second<num<first:
        second=num
   if second==float('-inf'):
      raise valueerror("No second largest number found.")
   return second
try:
   numbers=list(map(int,input("Enter numbers separated by spaces:").split()))
   print("Second largest number:",second_largest(numbers))
except valueerror as e:
   print("Error:",e)