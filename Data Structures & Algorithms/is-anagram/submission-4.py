class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Use a dictionary to track character frequencies
        count = {}
        
        for i in range(len(s)):
            # Increment for string s, decrement for string t
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        # If it's an anagram, every value in the dict must be 0
        for val in count.values():
            if val != 0:
                return False
                
        return True