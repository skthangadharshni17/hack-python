def rotate(lis,i):
   return lis[i:]+lis[:i]
lis=["apple","grapes","orange","cherry","mango"]
position=2
p=rotate(lis,position)
print(p)