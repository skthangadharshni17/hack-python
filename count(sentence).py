def count(sentence):
   words=sentence.split()
   return len(words)
sentence=input("Enter a sentence:")
word_count=count(sentence)
print("No.of words:",word_count)