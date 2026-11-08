class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total =  sum(nums)

        if abs(target) > total:
            return 0
        if (target + total) % 2 != 0:
            return 0 

        goal = (target + total) // 2

        n = len(nums)

        dp = [[0]*(goal+1) for _ in range(n +1)]

        dp[0][0] = 1

        for i in range(1,n+1):

            num = nums[i-1]

            for j in range(goal+1):

                if num > j:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-num]

        return dp[n][goal]







