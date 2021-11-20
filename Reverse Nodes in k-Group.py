def reverse(self, head, k):
        prevNode = None
        currNode = head
        c = 0
        while(currNode!=None and c<k):
            nextptr = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextptr
            c += 1
        if nextptr != None:
            head.next= self.reverse(nextptr,k)
        return prevNode
