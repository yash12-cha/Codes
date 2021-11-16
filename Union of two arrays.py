def doUnion(self,a,n,b,m):
        freq = {}
        for i in a:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in b:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        c = len(freq)
        return c
                
