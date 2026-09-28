class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if j > i+1 and b == nums[j -1]:
                    continue
                
                l = j+1
                r = len(nums) -1

                while l < r:
                    total = a +b +nums[l] +nums[r]

                    if total == target:
                        res.append([a,b,nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res
                    

