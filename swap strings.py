def swap(str1,str2):
   new_word1=str2[:1]+str1[1:]
   new_word2=str1[:1]+str2[1:]
   return new_word1+" "+new_word2
string1=input("Enter string1:")
string2=input("Enter string2:")
result=swap(string1,string2)
print("Result:",result)