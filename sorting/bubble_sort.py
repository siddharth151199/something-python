a=[]
n= int(input("enter size of array: "))
for i in range(0, n):
	x=int(input())
	a.append(x)
print(a)

def bubble_sort(a):
	for i in range(n):
		for j in range(0, n-i-1):
			if(a[j]>a[j+1]):
				temp= a[j]
				a[j]= a[j+1]
				a[j+1]= temp
bubble_sort(a)
print(a)
