def colours():
   colours=["Blue","Black","Red","Pink","Green"]
   l=len(colours)
   return l
def maxmin(lis):
   return min(lis),max(lis)
def sum_avg():
   s=sum(lis)
   avg=sum(lis)/len(lis)
   return s,avg
print("Size of the list colours:",colours())
lis=[10,20,30,40,50]
mini,maxi=maxmin(lis)
print("Minimum:",mini,"Maximum:",maxi)
total,avg=sum_avg()
print("Total:",total,"Average:",avg)