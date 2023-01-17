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
if r==c:
    print("Left Diagonal : ")
    for i in range(r):
        for j in range(c):
            if i==j:
                print(matrix[i][j])
    print("Right Diagonol")
    for i in range(r):
        for j in range(c):
            if i+j==r-1:
                print(matrix[i][j])
else:
    print("Diagonal not possible")
    print("Diagonal is only possible in square matrix")
