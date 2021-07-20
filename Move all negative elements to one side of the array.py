# Python program to move all negative elements to one side of the array.
def rearrange(arr, n ):
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print("\nResult : ",*arr)
n = int(input("Enter number of elements : "))
arr = list(map(int,input("\nEnter the elements : ").strip().split()))[:n]
rearrange(arr, n)
