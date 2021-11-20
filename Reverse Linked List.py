def reverseList(self, head):
        prevNode = None
        currNode = head
        while(currNode):
            nextptr = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextptr
        head = prevNode
        return head
