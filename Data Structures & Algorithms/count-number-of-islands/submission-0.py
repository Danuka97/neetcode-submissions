class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        def dfs(c,r):
            if (r < 0 or r >= row or
            c < 0 or c >= col or
            grid[r][c] != "1"):
                return

            grid[r][c] = "0"

            dfs(c,r+1)
            dfs(c,r-1)
            dfs(c+1,r)
            dfs(c-1,r)

        isiland =0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    isiland += 1
                    dfs(c,r)

        return isiland