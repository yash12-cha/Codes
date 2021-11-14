def countBitsFlip(self,a,b):
        value = a ^ b
        count = 0
        while (value):
            bits = value & 1
            if bits:
                count += 1
            value = value >> 1
        return count
