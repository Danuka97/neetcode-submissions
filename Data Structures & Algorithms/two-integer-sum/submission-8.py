class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff  in check:
                return[check[diff],i]
            else:
                check[a] = i