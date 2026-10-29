class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):

            pre1 = 0 
            pre2 = 0

            for i in range(len(nums)):
                curr = max(pre1 ,pre2 +nums[i])

                pre2 = pre1
                pre1 = curr

            return pre1

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[:-1]),helper(nums[1:]))