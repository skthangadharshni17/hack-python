def str_len(s):
   return len(s)
def concat_str(s1,s2):
   return s1+s2
#main routine
str1=input("Enter string1:")
str2=input("Enter string2:")
length1=str_len(str1)
length2=str_len(str2)
concat_string=concat_str(str1,str2)
print("Length of string1:",length1)
print("Length of string2:",length2)
print("Concatenated string:",concat_string)