class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        reults = nums[0]

        for i in range(1,len(nums)):
            n = nums[i]

            newmax = max(n,currmax * n, currmin *n)
            newmin = min(n,currmax * n, currmin *n)

            currmax = newmax
            currmin = newmin

            reults = max(reults,currmax)

        return reults