#PATTERN PROGRAMS--
n=int(input("enter number of rows "))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=' ')
	print()


#---
n=int(input("Enter number of rows"))
for i in range(1,n+1):
	print(str(i)*i)		#doesn't give spaces


#---
n=int(input("enter number of rows "))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i,end=' ')
	print()		#gives spaces


#---
n=int(input("enter number of rows "))
for i in range(0,n):
	for j in range(i,-1,-1):
		print(j+1,end=' ')
	print()


#---
n=int(input("enter number of rows "))
for i in range(n,0,-1):
	for j in range(1,n-i+2):
		print(i,end=' ')
	print()

#OR
#---
n=int(input("enter number of rows "))
for i in range(n):
	for j in range(i+1):
		print(n-i,end=' ')
	print()
