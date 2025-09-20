class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        j = 0
        for i in range(n):
            if i!= n-1 and nums[i]!=nums[i+1]:
                k+=1
                nums[j] = nums[i]
                j+=1
            elif i== n-1:
                nums[j] = nums[i]
        return k

            


        