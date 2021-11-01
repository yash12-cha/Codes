def Counting_Sort(Arr,N,pos):
    maxi = Arr[0]
    for i in range(N):
        if Arr[i] > maxi:
            maxi = Arr[i]
    Count = [0] * (maxi + 1)
    for i in range(N):
        index = Arr[i] // pos
        Count[index %10] = Count[index %10] + 1
    for i in range(1, maxi + 1):
        Count[i] = Count[i] + Count[i - 1]
    output = [0] * (N)
    for i in range(N - 1, -1, -1):
        index = Arr[i] // pos
        Count[index %10] -= 1
        output[Count[index % 10] - 1] = Arr[i]
    for i in range(N):
        Arr[i] = output[i]
    return Arr
def Radix_Sort(Arr,N):
    maxi = max(Arr)
    place = 1
    while maxi // place > 0:
        Counting_Sort(Arr, N,place)
        place *= 10
N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter array elements: ").strip().split()))
Radix_Sort(Arr,N)
print("Sorted Array: ",*Arr)
