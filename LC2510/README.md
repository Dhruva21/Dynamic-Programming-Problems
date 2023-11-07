# Problem Statement
You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1).
Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.

Example 1:
Input: grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
Output: true
Explanation: The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.
Example 2:
Input: grid = [[1,1,0],[0,0,1],[1,0,0]]
Output: false
Explanation: There is no path in this grid with an equal number of 0's and 1's.
 
Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 100
grid[i][j] is either 0 or 1.

# Solution

# 1. Brute force --> using recursion.
This is a typical dp on grid problem. Which can be tried using recursion, by exploring all the path.
Let Function f(i, j, n, m, summ) be the recursive function which returns True/False. summ is used to keep track the summ of all the visited paths.

## Base Case
1. Out of Bounds case, two directions possible --> hence towards right or down return False
2. If target is reached (n-1,m-1), we need to return true if n+m-1 == 2*summ (checking the equality of 1's and 0's).

## Explore all path
From each block there are two possible ways to traverse. Right (row, col+1) and down (row+1, col)
down = f(i+1, j, n, m, summ+grid[i][j])
right = f(i, j+1, n, m, summ+grid[i][j])

## Final answer
return down or right

# Optimized
If we draw a recursive tree, we could encounter repetitive sub problems. We can store the values of previously computed (i, j, summ) and reuse those values.


