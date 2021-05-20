def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_lists(left,right)
def merge_two_sorted_lists(a,b):
    sorted_list=[]
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i = i + 1
        else:
            sorted_list.append(b[j])
            j = j + 1
    while i < len_a:
        sorted_list.append(a[i])
        i = i + 1
    while j < len_b:
        sorted_list.append(b[j])
        j = j + 1

    return sorted_list
print("Merge Sort: ")
l= [10,3,15,7,8,23,98,29]
print(merge_sort(l))