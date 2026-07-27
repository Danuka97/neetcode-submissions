class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False
        
        def counters(s):
            s_dict = {}
            for i in s:
                if i in s_dict:
                    s_dict[i] +=1
                else:
                    s_dict[i] = 1
            return s_dict
        return counters(s) == counters(t)