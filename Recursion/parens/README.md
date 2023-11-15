Problem Statement:
Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parantheses.   
Example:
Input: n = 3
Output: ((())), (()()), (())(), ()(()), ()()()

## Recursive Approach
On each recursive call, we have the index for a particular character in the string. We need to select either a left or a right parens, as long as our expression stays valid.

1. Left Paren: As long as we haven't used up all the left parantheses, we can always insert a left paren.
2. Right Paren: We can insert a right paren as long as it won't lead to a syntax error. When will we get a syntax error? We will get a syntax error if there are more right parantheses than left.

So, we simply keep track of the number of left and right parentheses allowed. If there are left parens remaining, we'll insert a left paren and recurse. If there are more left(i.e., if there are more left parens in use than right parens), then we'll insert a right paren and recurse.