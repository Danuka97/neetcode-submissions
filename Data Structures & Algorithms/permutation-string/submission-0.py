class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        s2_count = {}

        for i in s1:
           s1_count[i] =  s1_count.get(i,0) +1
        
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            s2_count[c] =  s2_count.get(c,0) +1

            if r - l +1 > len(s1):
                l_chr= s2[l] 
                s2_count[l_chr] -= 1

                if s2_count[l_chr] == 0:
                    del s2_count[l_chr]
                l += 1
            
            if s1_count == s2_count:
                return True
        
        return False




        