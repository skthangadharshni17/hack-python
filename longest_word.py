def longest_word(sentence):
   words=sentence.split()
   long_word=max(words,key=len)
   return long_word
text=input("Enter a sentence:")
long_word=longest_word(text)
print("Longest words:",long_word)