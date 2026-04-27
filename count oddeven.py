def count_even_odd():
   num=input("Enter numbers separated by spaces:").split()
   num=[int(nums)for nums in num]
   odd=sum(1 for nums in num if nums%2!=0)
   even=len(num)-odd
   print("Odd numbers:",odd)
   print("Even numbers:",even)
count_even_odd()