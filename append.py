def append():
   odd=[x for x in range(1,limit+1)if x%2!=0]
   even=[x for x in range(1,limit+1)if x%2==0]
   combined_list=odd+even
   return combined_list
limit=int(input("Enter the limit:"))
p=append()
print(p)