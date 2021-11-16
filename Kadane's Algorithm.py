def maxSubArraySum(self,arr,N):
        maxi = -float('inf')
        max_till_here = 0
        for i in range(0,N):
            max_till_here = max_till_here + arr[i]
            if max_till_here > maxi:
                maxi = max_till_here
            if max_till_here < 0:
                max_till_here = 0
        return maxi
