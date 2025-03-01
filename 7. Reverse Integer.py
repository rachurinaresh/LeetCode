class Solution:
    def reverse(self, x: int) -> int:
        r=""
        s = str(x)
        if s[0] == '-':
            r=s[:0:-1]
        else:
            r=s[::-1]
        if int(r) <=((2**31) - 1):
            if s[0] == '-':
                return -int(r)
            else:
                return int(r)
        return 0