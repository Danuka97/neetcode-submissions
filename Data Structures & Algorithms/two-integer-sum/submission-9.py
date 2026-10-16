class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

        for i,a in enumerate(nums):
            diff = target - nums[i] 
            if diff not in res:
                res[a] = i 
            else:
                return[res[diff],i]