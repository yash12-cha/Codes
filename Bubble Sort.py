# Implementation of Bubble Sort
N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter elements: ").strip().split()))[:N]
# Number of passes will be 'N - 1'
for i in range(N-1):
    swapped = False
    # Since, after each iteration righmost i elements are sorted 
    for j in range(0,N - i - 1):
        if Arr[j] > Arr[j+1]:
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp
            swapped = True
    # If no number was swapped that means array is sorted now, break the loop.
    if swapped == False:
        break
print("Sorted Array: ",*Arr)

    
