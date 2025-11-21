class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1:
            if n in cycle:
                return False
            cycle.add(n)
            new_n = 0
            for i in str(n):
                new_n += int(i)**2
            n = new_n            
        return True 