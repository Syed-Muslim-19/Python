number=input("Write a non-zero number: ")
num=int(number)
rem=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c0=0
cc=0
for i in range(num):
    rem=num%10
    if rem>0:
        cc+=1
    if rem==1:
        c1+=1
    elif rem==2:
        c2+=1
    elif rem==3:
        c3+=1
    elif rem==4:
        c4+=1
    elif rem==5:
        c5+=1
    elif rem==6:
        c6+=1
    elif rem==7:
        c7+=1
    elif rem==8:
        c8+=1
    elif rem==9:
        c9+=1
    num=num//10

print("The Frequency of 0 is : "+str(len(str(number))-cc))
print("The Frequency of 1 is : "+str(c1))
print("The Frequency of 2 is : "+str(c2))
print("The Frequency of 3 is : "+str(c3))
print("The Frequency of 4 is : "+str(c4))
print("The Frequency of 5 is : "+str(c5))
print("The Frequency of 6 is : "+str(c6))
print("The Frequency of 7 is : "+str(c7))
print("The Frequency of 8 is : "+str(c8))
print("The Frequency of 9 is : "+str(c9))