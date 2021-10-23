def MAX_HEAPIFY(A,N,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < N and A[largest] < A[l]:
          largest = l
    if r < N and A[largest] < A[r]:
          largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A,N,largest)
def BUILD_MAX_HEAP(A,N):
    for i in range(N//2-1,-1,-1):
        MAX_HEAPIFY(A,N,i)
def HEAP_SORT(A,N):
    BUILD_MAX_HEAP(A,N)
    for i in range(N-1,-1,-1):
        A[i],A[0] = A[0], A[i]
        MAX_HEAPIFY(A,i,0)
N = int(input("Enter number of elements: "))
A = list(map(int,input("Enter array elements: ").strip().split()))
HEAP_SORT(A,N)
print("Sorted Array: ",*A) 
