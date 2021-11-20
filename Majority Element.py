def majorityElement(self, A):
        N = len(A)
        freq = {}
        for i in A:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in freq:
            if freq[i] > N/2:
                return i
        else:
            return -1
