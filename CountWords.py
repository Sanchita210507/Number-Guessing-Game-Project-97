abc=input("enter a sentence: ")
wordcount=0
charactercount=0
for i in abc:
    charactercount=charactercount+1
    if(i==" "):
        wordcount=wordcount+1
print("number of words in the sentence: ")
print(wordcount+1)
print("number of characters in the sentence: ")
print(charactercount)