class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        
        def recursive(x, y, dungeon, n, m, memo):
            if (x, y) in memo:
                return memo[(x,y)]
            if x == n or y == m:
                return 2**31
            if x == n - 1 and y == m - 1:
                if dungeon[x][y] <= 0:
                    return -dungeon[x][y] + 1
                return 1
            
            bottom = recursive(x + 1, y, dungeon, n, m, memo)
            right = recursive(x, y + 1, dungeon, n, m, memo)
            minHealth = min(bottom, right) - dungeon[x][y] 
            if minHealth <= 0:
                memo[(x,y)] = 1
            else:
                memo[(x,y)] = minHealth
            return memo[(x,y)]
        n = len(dungeon)  
        m = len(dungeon[0])
        
        return recursive(0, 0, dungeon, n , m, {})     