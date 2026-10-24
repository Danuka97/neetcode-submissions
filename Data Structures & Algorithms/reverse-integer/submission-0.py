class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sing = -1 if x < 0 else 1

        x = abs(x)

        while x > 0:
            digt  = x % 10
            res = res *10 + digt

            x = x//10

        res = res*sing

        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return res