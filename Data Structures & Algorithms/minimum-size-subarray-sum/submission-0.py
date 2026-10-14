class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        wind = float('inf')
        total = 0

        for r in range(len(nums)):
            total += nums[r]


            while total >= target:
                wind = min(wind,r-l+1)
                total -= nums[l]

                l += 1
        return 0 if wind == float('inf') else wind


                

        