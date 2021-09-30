# Implementation of Selection Sort
N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter elements: ").strip().split()))[:N]
for i in range(0,N-1):
    mini = i
    for j in range(i+1,N):
        if Arr[j] < Arr[mini]:
            mini = j
        temp = Arr[i]
        Arr[i] = Arr[mini]
        Arr[mini] = temp
print("Sorted Array: ",*Arr)
        
