class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0
        x = abs(x)
        rev = 0
        while x>0:
            rev = rev*10 + x%10
            x //= 10
        if rev >= -1*(2**31) and rev<= (2**31 -1):
            if is_neg:
                return -1*rev
            else:
                return rev
        return 0