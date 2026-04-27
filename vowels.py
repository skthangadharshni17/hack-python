
def count_vowel(string):
   vowels="aeiouAEIOU"
   count=sum(1 for char in string if char in vowels)
   return count

#main routine
text=input("Enter string:")
print("No.of vowels:",count_vowel(text))