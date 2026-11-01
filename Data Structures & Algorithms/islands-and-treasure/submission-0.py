from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()

        row ,col = len(grid),len(grid[0])

        INF = 2147483647

        dire = directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        for c in range(col):
            for r in range(row):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:

            r,c = queue.popleft()

            for dr,dc in dire:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < row and
                    0 <= nc < col and
                    grid[nr][nc] == INF):

                    grid[nr][nc] = 1+ grid[r][c]

                    queue.append((nr,nc))

        return None

