def isPalindrome(self, S):
	    str = ""
        for i in S:
            str = i + str
        if str == S:
            return 1
        else:
            return 0
