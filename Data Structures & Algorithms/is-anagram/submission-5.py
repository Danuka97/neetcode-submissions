from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This is O(n) but runs at C-speed
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)