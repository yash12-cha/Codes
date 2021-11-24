def rotateString(self, s, goal):
        l1 = len(s)
        l2 = len(goal)
        if l1 != l2:
            return False
        else:
            temp = s + s
            if temp.count(goal) > 0 :
                return True
            else:
                return False
