def duplicates(lis):
   lst=[]
   for i in lis:
      if i not in lst:
       lst.append(i)
   return lst
lis=[1,2,2,3,4,4,5,6,6,7]
print(duplicates(lis))