def partition(A,left,right):
    pivot = left
    i = left
    j = right
    while i < j:
        while (A[i] <= A[pivot]):
            i = i + 1
        while(A[j]>A[pivot]):
            j= j - 1
        if i < j:
            temp=A[i];
            A[i]=A[j];
            A[j]=temp;
    temp=A[pivot];
    A[pivot]=A[j];
    A[j]=temp;
    return j
    
def quickSort(A,left,right):
    if left < right:
        pi = partition(A,left,right)
        quickSort(A,left,pi-1)
        quickSort(A,pi+1,right)
N = int(input("Enter number of elements: "))
A = list(map(int,input("Enter array elements: ").strip().split()))
quickSort(A,0,N-1)
print("Sorted Array: ",*A) 
