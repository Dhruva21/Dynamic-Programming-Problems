# Problem : LC1980. Find Unique Binary String

# Problem Statement
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

# Approach
Recursively iterate through all the possible binary strings of length n. This takes 2^n possible ways.

Base Case: When the string of length n is formed check whether it is present in nums or not.

We can reduce the unwanted recursive calls, as stated in the problem statement there are n strings of each length n. Hence at the worst case we need to iterate through n+1 times to find out the answer. In the code snippet there is a check for add_zero, after adding zero if the function returns a valid string then we can ignore the next recursive call to add_one.

# Time Complexity
O(N^2)

# Space Complexity
O(N) --> recursive call stack