N=int(input("Write a positive number : "))
A=float(input("The Guess of square root : "))
for i in range(10):
	A=(A+(N/A))/2
	print("The next better approximation is : " + str(A))
