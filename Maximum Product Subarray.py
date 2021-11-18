def maxProduct(self,arr, n):
	    ans = arr[0]
		ma = arr[0]
		mi = arr[0]
		
		for i in range(1,n):
		    if arr[i] < 0:
		        ma,mi = mi,ma
		    ma = max(arr[i],ma*arr[i])
		    mi = min(arr[i],mi*arr[i])
		    ans = max(ans,ma)
		return ans
