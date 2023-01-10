word=[]
leng=int(input("Input the Length of List : "))
for i in range(leng):
    word.append(input("Write any word : "))
search=input("Enter the word to be search : ")

if search in word:
    print("Word is in the list")
else:
     print("Word is in not in the list")

    