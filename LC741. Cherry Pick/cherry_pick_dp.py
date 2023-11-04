class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # populate all combinations of paths
        possible_paths = [[1,0,1,0], [0,1,0,1], [1,0,0,1], [0,1,1,0]]
        def recursive(grid, r1, c1, r2, c2, n, memo):
            # check if already present in memo dict
            if (r1,c1,r2,c2) in memo:
                return memo[(r1,c1,r2,c2)]

            # base cases
            # reaching the last row
            if r1 == n - 1 and r2 == n - 1 and c1 == n - 1 and c2 == n - 1:
                return grid[r1][c1]
            
            # out of bounds case to the right side of the matrix
            if c1 >= n or c2 >= n:
                return -2**31
            
            # store current cell value
            ret = 0
            # if both fall on the same cell
            if r1 == r2 and c1 == c2:
                ret += grid[r1][c1]
            else:
                ret += grid[r1][c1] + grid[r2][c2]
            
            maxi = -2**31
            for path in possible_paths:
                x1 = r1 + path[0]
                y1 = c1 + path[1]
                x2 = r2 + path[2]
                y2 = c2 + path[3]
                if x1 >= n or y1 >= n or x2 >= n or y2 >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
                    continue
                maxi = max(maxi, recursive(grid, x1, y1, x2, y2, n, memo))
            ret += maxi
            memo[(r1,c1,r2,c2)] = ret
            return memo[(r1,c1,r2,c2)]

        
        ans = recursive(grid, 0, 0, 0, 0, len(grid), {})
        if ans < 0:
            return 0
        return ans