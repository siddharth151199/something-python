arr=[]
n=int(input("Enter size of array: "))
for i in range(n):
	val=int(input("Enter value: "))
	arr.append(val)
print(arr)
arr.sort()
print("The sorted elements are: ")
print(arr)
