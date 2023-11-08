class Solution:
    def isThereAPath(self, grid) -> bool:
        
        def recursion(i, j, n, m, summ, memo):
            if (i, j, summ) in memo:
                return memo[(i, j, summ)]
            # out of bounds case
            if i >= n or j >= m:
                return False
            # when reached the target last block (n-1,m-1)
            if i == n-1 and j == m-1:
                summ += grid[i][j]
                if (n + m -1)  == 2*summ:
                    return True
                return False
            
            # exlpore all paths (right and down)
            right = recursion(i, j+1, n, m, summ+grid[i][j], memo)
            down = recursion(i+1, j, n, m, summ+grid[i][j], memo)

            memo[(i, j, summ)] = right or down
            return memo[(i, j, summ)]
        
        n = len(grid)
        m = len(grid[0])

        return recursion(0, 0, n, m, 0, {})