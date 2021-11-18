def findMinDiff(self, A,n,m):
        A.sort()
        mi = float('inf')
        for i in range(n-m+1):
            if (A[i+m-1] - A[i]) < mi:
                mi = A[i+m-1] - A[i]
        return mi
