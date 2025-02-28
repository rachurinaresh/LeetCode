class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        d = 0
        copied_list = nums[:]
        copied_list1 = nums[:]
        nums.sort()
        i = 0
        j = n - 1
        while i < j and i < n -1 and i >= 0 and j < n :
            if nums[i] + nums[j] == target :
                break
            elif nums[i] + nums[j] > target :
                j=j-1
            else:
                i=i+1
        copied_list1.reverse()
        return [copied_list.index(nums[i]),n - copied_list1.index(nums[j]) - 1]

            