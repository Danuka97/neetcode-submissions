class Solution:
    def isPalindrome(self, x: int) -> bool:

        nums = str(x)


        l = 0 
        r = len(nums) -1

        if len(nums) == 1:
            return True

        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


            
        