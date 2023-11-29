# problem Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

# Intution
# Brute Force 
Traverse through each and every substring in the entire string and check whether that string is a palindrome or not.

Time complexity: O(N^3)
Space complexity: O(1)

# Optimizing using DP table.
if s[i:j] is a palindrome two conditions needs to be satisfied: s[i] == s[j] and s[i+1:j-1] is also a palindrome.

Here s[i+1:j-1] is precomputed in the dp table. 
Hence we need to fill the upper traingle of the 2d array column-wise. 

Base cases.
1. compute one length string, we can say that it is palindrome. Hence all the diagonal elements in dp becomes 1.
2. compute two length strings, the cell becomes 1 if s[i] == s[i+1] --> used for even length palindromes.

Time complexity: O(N^2)
Space complexity: O(N^2)
