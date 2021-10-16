from math import sqrt
x = int(input("Enter the number: "))
result = []   # We will store all factors in `result`
i = 1
# This will loop from 1 to int(sqrt(x))
while i <= int(sqrt(x)):
    if x % i == 0:     # Check if i divides x without leaving a remainder
        result.append(i)
        # Handle the case explained in the 4th (Refer Document)
        if x//i != i:
            result.append(x//i)
    i += 1
print("Factors of the given number are: ",*result)