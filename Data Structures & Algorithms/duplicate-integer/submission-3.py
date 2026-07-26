class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        uniqe = set()

        for i in range(len(nums)):
            if nums[i] in uniqe:
                return True
            else:
                uniqe.add(nums[i])

        return False
        