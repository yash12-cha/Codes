print("Enter List elements: ")
lis = list(map(int,input().split()))
lis.sort()
print("Largest number in the list is: ",lis[-1])
