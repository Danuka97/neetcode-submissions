from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row,col = len(grid),len(grid[0])

        queue = deque()
        fresh = 0
        mui = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for c in range(col):
            for r in range(row):
                if grid[r][c] == 2:
                     queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            # r,c = queue.popleft()

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr,dc in directions:
                    nc = c +dc
                    nr = r+dr

                    if (0 <= nr < row and
                        0 <= nc < col and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            mui += 1

        return mui if fresh == 0 else -1
                


        