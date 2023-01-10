word=[]
leng=int(input("Input the Length of List : "))
for i in range(leng):
    word.append(input("Write any word : "))
    
print(word)
Del=input("Enter the word to be Deleted : ")
if Del in word:
    word.remove(Del)
    print(word)
else:
    print("Word not Found ")

    