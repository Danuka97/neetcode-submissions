class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_set =dict()
        for i, n in enumerate(nums):
            diff = target -n
            
            if diff in data_set:
                return [data_set[diff], i]
            data_set[n] = i
        return[]