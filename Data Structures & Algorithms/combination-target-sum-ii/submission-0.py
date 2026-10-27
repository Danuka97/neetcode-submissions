class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        sub = []
        res = []

        def dfs(i,tol):
            if tol == target:
                res.append(sub.copy())
                return
            if tol > target or i ==len(candidates):
                return

            sub.append(candidates[i])

            dfs(i+1,tol + candidates[i])

            sub.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1,tol)

        dfs(0,0)
        return res