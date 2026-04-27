def is_prime(n):
   if (n<2):
      return 0
   for i in range(2,int(n**0.5)+1):
      if n%i==0:
         return 0
   return 1

#main routine
num=int(input("Enter a number:"))
print("Print 1 for prime otherwise print 0:",is_prime(num))