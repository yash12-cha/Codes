# Shell sort in python
n = int(input("Enter number of elements: "))
array = list(map(int,input("Enter array elements: ").strip().split()))
# Rearrange elements at each n/2, n/4, n/8, ... intervals
interval = n // 2
while interval > 0:
    for i in range(interval, n):
        temp = array[i]
        j = i
        while j >= interval and array[j - interval] > temp:
            array[j] = array[j - interval]
            j -= interval
        array[j] = temp
    interval //= 2
print("Sorted Array: ",*array)
