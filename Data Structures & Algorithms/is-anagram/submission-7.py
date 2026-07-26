class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def count(s):
            counts = {}
            for i in s:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
            return counts
        return count(s) == count(t)