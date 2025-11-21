class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        s = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i] >= s:
                s = i
        if s == 0:
            return True
        else:
            return False

