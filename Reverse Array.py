N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter elements: ").strip().split()))
start = 0
end = N - 1
while(start < end):
    Arr[start],Arr[end] = Arr[end],Arr[start]
    start += 1
    end -= 1
print("Reverse Array:",*Arr)
