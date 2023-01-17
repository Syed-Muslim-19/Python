matrix=[]
r=int(input("Write the number of rows : "))
c=int(input("Write the number of columns : "))
for i in range(r):
    element=[]
    for j in range(c):
        entity=int((input(str(i+1)+" Row and " + str(j+1)+" Column : ")))
        element.append(entity)
    matrix.append(element)
print("The Matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()