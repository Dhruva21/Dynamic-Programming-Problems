class Solution:
    def minPathSum(self, grid) -> int: 
        n = len(grid)
        m = len(grid[0])
        # dp = [[0 for _ in range(m)] for _ in range(n)]
        prev = [0 for _ in range(m)]
        for i in range(n):
            cur = [0 for _ in range(m)]
            for j in range(m):
                if i == 0 and j == 0:
                    cur[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up += 2**31
                    left = grid[i][j]
                    if j > 0:
                        left += cur[j-1]
                    else:
                        left += 2**31
                    cur[j] = min(up, left)
            prev = cur
        return prev[m-1]