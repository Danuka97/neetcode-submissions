class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        expact = n * (n+1)//2
        act = sum(nums)

        return expact - act
        