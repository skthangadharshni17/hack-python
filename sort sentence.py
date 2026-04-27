def sort_sentence(sentence):
   words=sentence.split()
   words.sort()
   sorted_sentence=" ".join(words)
   return sorted_sentence
#main routine
text=str(input("Enter a sentence:"))
sorted_result=sort_sentence(text)
print("Sorted sentence:",sorted_result)