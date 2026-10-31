class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row,col = len(grid),len(grid[0])

        def dfs(r,c):
            if (r <0 or r >= row or c < 0 or c >= col or grid[r][c] == 0):
                return 0


            grid[r][c] = 0

            

            return (1+ dfs(r+1,c) + dfs(r-1,c) +dfs(r,c+1) +dfs(r,c-1))

        a = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    newA = dfs(r,c)
                    a = max(newA,a)

        return a



        
        