def getMinMax( a, n):
    if n == 1:
        max = a[0]
        min = a[0]
    else:
        if a[0] > a[1]:
            max = a[0]
            min = a[1]
        else:
            max = a[1]
            min = a[0]
        for i in range(2,n):
            if a[i] > max:
                max = a[i]
            if a[i] < min:
                min = a[i]
    
    return max,min
