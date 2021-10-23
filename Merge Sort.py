# Merge Sort
def merge(Arr,l,mid,r):
    n1 = mid-l+1
    n2 = r -mid
    a = [0]*n1
    b = [0]*n2
    for i in range(0,n1):
        a[i] = Arr[l+i]
    for j in range(0,n2):
        b[j] = Arr[mid+1+j]
    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if a[i] < b[j]:
            Arr[k] = a[i]
            k = k + 1
            i = i + 1
        else:
            Arr[k] = b[j]
            k = k + 1
            j = j + 1
    while i < n1:
        Arr[k]= a[i]
        k =k + 1
        i = i + 1
    while j < n2:
        Arr[k] = b[j]
        k =k + 1
        j = j + 1
def mergeSort(A,l,r):
    if l < r:
        mid = (l+r)//2
        mergeSort(A,l,mid)
        mergeSort(A,mid+1,r)
        merge(A,l,mid,r)
n = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter array elements: ").strip().split()))
mergeSort(Arr,0,n-1)
print("Sorted Array: ",*Arr)
        
    
