class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        r_w1 = len(word1)
        r_w2 = len(word2)

        res = []

        R = min(r_w1,r_w2)

        while l < R:
            res.append(word1[l])
            res.append(word2[l])
            l += 1
        res.append(word1[l:])
        res.append(word2[l:])
        return "".join(res)


