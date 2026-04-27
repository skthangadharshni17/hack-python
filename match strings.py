def match(words):
   count=0
   for word in words:
      if len(word)>=2 and word[0]==word[-1]:
       count+=1
   return count
lst=input("Enter the words separated by spaces:").split()
result=match(lst)
print("Count of matching strings:",result)