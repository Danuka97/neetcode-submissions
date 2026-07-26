class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        data = set(nums)
        longest_streak = 0

        for i in data:
            if i-1 not in data:
                current_num = i
                current_streak = 1

                while (current_num+1) in data:
                    current_num += 1
                    current_streak = current_streak+1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak