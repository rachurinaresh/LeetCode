class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j = 0
        for i in nums:
            if i != val:
                k+=1
                nums[j] = i
                j+=1
        return k
        