matrix=[]
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
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The Transose form :")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()