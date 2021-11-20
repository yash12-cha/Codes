def removeDuplicates(head):
    main = head
    if main == None:
        return None
    while main.next:
        if main.data == main.next.data:
            main.next = main.next.next
        else:
            main = main.next
	return head
