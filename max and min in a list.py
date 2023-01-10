number=int(input("Enter the range of List : "))
num=[]
for i in range(number):
    num.append(int(input("Enter the Numbers : ")))
    
maximum=num[0]
for i in range(number):
    if maximum<num[i]:
        maximum=num[i]
print("The Maximum number is : "+ str(maximum))
minimum=num[0]
for i in range(number):
    if minimum>num[i]:
        minimum=num[i]
print("The Manimum number is : "+ str(minimum))