def setBits(self, N):
	    count = 0
	    while N:
	        bit = N & 1
	        if bit:
	            count += 1
	        N = N >> 1
	    return count
