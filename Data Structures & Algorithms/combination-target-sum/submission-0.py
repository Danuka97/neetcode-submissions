class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sub = []
        res = []

        def dfs(i,tol):

            if tol == target:
                res.append(sub.copy())
                return
            if tol > target or i ==len(nums):
                return

            sub.append(nums[i])

            dfs(i,tol + nums[i])

            sub.pop()

            dfs(i+1,tol)

        dfs(0,0)

        return res
            

            
                

