sentence=input("Sentence : ").split()
word=input("The word to count : ")
count=0
for i in range(len(sentence)):
    if(sentence[i]==word):
        count+=1
if count==0:
    print("Word not found")
else:
    print("The Frequency of word in the sentence : "+str(count))