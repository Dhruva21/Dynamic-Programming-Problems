class Solution:
    def minPathSum(self, grid) -> int:
        
        def memoization(grid, i, j, memo):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                return grid[i][j]
            # out of bounds
            if i < 0 or j < 0:
                return 2**31
            
            # explore all paths
            up = grid[i][j] + memoization(grid, i-1, j, memo)
            left = grid[i][j] + memoization(grid, i, j-1, memo)

            memo[(i,j)] = min(up, left)
            return memo[(i,j)]

        m=len(grid)-1
        n=len(grid[0])-1
        return memoization(grid, m, n, {})
