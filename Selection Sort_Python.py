# Python Program for Selection Sort

# Unsorted List
A=[64,25,3,49,1]

# Traverse through all array elements
for i in range(len(A)):
    min = i
    for j in range(i+1,len(A)):
        if A[min] > A[j]:
            min = j
    # Swapping
    temp= A[i]
    A[i] = A[min]
    A[min] = temp
print("Sorted Array: ")
for i in range(len(A)):
    print(A[i])

    