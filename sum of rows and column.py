matrix=[]
summ=0
r=int(input("Rows : "))
c=int(input("Column : "))
for i in range(r):
    l=[]
    for j in range(c):
        val=int(input(str(i+1)+" Row and "+str(j+1)+" Column : "))
        l.append(val)
    matrix.append(l)
print("The Matrix form :")
for i in range(r):
    sumr=0
    for j in range(c):
        print(matrix[i][j],end=" ")
        summ+=matrix[i][j]
    print()
for i in range(r):
    sumr=0
    for j in range(c):
        sumr+=matrix[i][j]
    print("The Sum of Row "+str(i+1)+" is : "+str(sumr))
for i in range(r):
    sumc=0
    for j in range(c):
        sumc+=matrix[j][i]
    print("The Sum of Column "+str(i+1)+" is : "+str(sumc))
print("The sum of total elements are : " + str(summ))
