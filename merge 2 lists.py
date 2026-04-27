
def merge(list1,list2):
   m=list1+list2
   m.sort()
   return m
list1=['a','v','l']
list2=['d','t','f']
print("Sorted list:\n",merge(list1,list2))