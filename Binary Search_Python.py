A = [2,4,5,6,7,8]
key = int(input("Enter the element to be searched: "))
first = 0
last = len(A) - 1
mid = int((first + last) / 2)
while ( last >= first):
    if ( A[mid] < key):
        first = mid + 1
    elif ( A[mid] == key):
        print(key,"found at position",mid,".")
        break
    else:
        last = mid - 1
    mid = int((first + last) / 2)
if (first > last):
    print("Element not found!!!")
