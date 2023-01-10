print("Find the sum of series n+nn+nnn......+n^n")
number=int(input("Input the number: "))
summ=0
pro=number
for i in range(number):
    summ=pro+summ
    pro=number*pro
    
print("The sum of the series : "+ str(summ))