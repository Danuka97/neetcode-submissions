class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            a = sorted(s)
            b = sorted(t)
            return a==b
        else:
            return False
        
        