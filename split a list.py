
def split_list(m,n):
   data=[]
   for i in range(m):
      data.append(i+1)
   size=m//n
   chunks=[]
   for i in range(0,m,size):
      chunks.append(data[i:i+size])
   return chunks
res=split_list(10,2)
print(res)