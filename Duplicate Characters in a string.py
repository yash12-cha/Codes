s = input("Enter any String: ")
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in freq:
    if freq[i] > 1:
        print("Character: ",i,",","Frequency: ",freq[i])
        
