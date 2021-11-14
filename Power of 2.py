def isPowerofTwo(self,n):
        m = n - 1
        val = n & m
        if n == 0:
            return False
        if val == 0:
            return True
        else:
            return False
