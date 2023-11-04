# Explanation about LC:741 Cerry Pick problem.


By referring to striver's 3D Dp concept explanation for the problem maximum chocolates alice and bob can get if alice starts from top left and bob starts from top right. They have three paths to move left-diagonal, down and right-diagonal.
Youtube link: https://www.youtube.com/watch?v=QGfn7JeXK54&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16
            
Came up with a recursive solution exploring all paths considering two people starting from (0, 0) and to reach (n-1, n-1), they have two ways to traverse(right, down) 
For optimization, there are repetitive subproblems and hence there are four indices for which the state is stored and can be reused to populate the result.  
4D dp matrix is used for optimization.
