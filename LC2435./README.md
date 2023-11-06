# Description of LC2435. Paths in Matrix Whose Sum Is Divisible by K
Problem Link:
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/

Problem Statement:
Task is to find the total number of paths starting from (0,0) to (n-1,m-1) whose path sum is divisible by k. Only possible ways to go from one cell is towards right and down.

# Approach:

# Brute Force:
Thinking the problem in terms of recursion. First explore all the paths to the right and down. Compute the number of paths going in both directions. Make sure to keep track of path sum till a particular index.(i,j)
Let grid be the matrix
Let recursive function f(i, j, summ) --> initially pass (0,0). We can do either ways from last index to start as well. 
# Base Case:
1. As there are two possible ways towards right and down, we could land and go into out of bounds.
2. When we reach target index check the summ + target index value is divisible by 3. If yes return 1 else return 0

# Explore all the paths:
right = f(i, i+1, summ + grid[i][j])<br>
down = f(i+1, j, summ + grid[i][j])

# Final answer 
sum of both paths right and down

# Time and space complexity
From each cell there are two possible ways to traverse. Towards right and down.
TC = O(2**n)
SC = O(N) --> Auxiliary stack space it require maximum of N

```
If we try to draw the recursive tree then we will encounter there are repetitive subproblems for this question. Hence We can store the values of (i, j, summ) and reuse it whenever we encounter the other time. We can use 3D array dp to store the values or in python we can store the tupe (i, j, summ) 
```

# Time and space complexity after memoization

TC = O(m*n*k) <br>
SC = O(n) --> Auxiliary Stack Space

# Python code snippet which gave Memory limited exceeded

```
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        def recursive(i, j, summ, memo):
            # check if tuple (i, j, summ) already present in memo
            if (i, j, summ) in memo:
                return memo[(i, j, summ)] % (10**9 + 7)
            # base cases
            # OOB --> i,j going out of bounds
            if i >= n or j >= m:
                return 0
            # reached target n-1,m-1
            if i == n-1 and j == m-1:
                if (summ + grid[i][j]) % k == 0:
                    return 1
                return 0
            
            # explore all the paths --> right and down
            right = recursive(i, j+1, (summ + grid[i][j]) % (10**9 + 7), memo)
            down = recursive(i+1, j, (summ + grid[i][j]) % (10**9 + 7), memo)
            memo[(i, j, summ)] = (right + down) % (10**9 + 7)
            return memo[(i, j, summ)]
        
        n = len(grid)
        m = len(grid[0])
        return recursive(0, 0, 0, {})
```