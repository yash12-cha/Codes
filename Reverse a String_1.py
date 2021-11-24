def reverseWord(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
  # In above code, we call a function to reverse a string, which iterates to every element and intelligently join each character in the beginning so as to obtain the reversed string.
