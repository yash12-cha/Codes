def removeDuplicates(self, head):
        freq = {}
        curr = head
        prev = curr
        while(curr):
            if curr.data in freq:
                prev.next = curr.next
            else:
                freq[curr.data] = 1
                prev = curr
            curr = curr.next
        return head
