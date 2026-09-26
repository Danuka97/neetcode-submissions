class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        seen = set()

        while l < r:
            diff = numbers[r] + numbers[l]

            if diff == target:
                return [l+1,r+1]

            elif diff < target:
                l += 1
            else:
                r -= 1