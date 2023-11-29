class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # the below table holds whether the string s[i:j] is a palindrome or not.
        dp = [[0 for i in range(n)] for j in range(n)]
        ans = [0, 0]
        # base case 1 - one length string
        for i in range(n):
            dp[i][i] = 1
            ans = [i, i]
        
        # base case 2 - two length string
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans = [i, i + 1]
        # fill the dp table
        for j in range(n):
            for i in range(j):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    if (j - i + 1) > (ans[1] - ans[0] + 1):
                        ans[0] = i
                        ans[1] = j
        
        return s[ans[0]:ans[1]+1]