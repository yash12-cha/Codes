def hasCycle(self, head):
        if head == None:
            return False
        freq = {}
        while(head):
            if head not in freq:
                freq[head] = 1
                head = head.next
            else:
                return True
        return False
            
