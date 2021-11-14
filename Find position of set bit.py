def findPosition(self, N):
        if N == 0:
            return -1
        if (N & (N-1)) == 0:
            count = 0
            while(N):
                bit = N & 1
                count += 1
                N = N >> 1
            return count
        else:
            return -1
