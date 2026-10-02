class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) -1
        nums.sort()
        max_res = -1

        while l < r:
            total = nums[l] + nums[r] 
            if total < k:
                l += 1
                max_res = max(max_res,total)

            else:
                r -= 1
        return max_res

                
