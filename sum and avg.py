def sum_avg(*args):
   n=len(args)
   s=0
   for i in range(n):
      s=s+args[1]
      av=s/n
      return s,av

#main routine
total,avg=sum_avg(10,20,30,40,50)
print("Sum",total,"Average",avg)