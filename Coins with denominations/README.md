# Problem statement
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.

# Solution
1. Brute force --> Recursively traverse through all possible ways to make sum n with combination of denomiations.
Let f(n, denoms, index) be recursive function.
    Base case:
        1. last denom if index >= len(denoms) - 1 then return 1 (one way)
    denomAmount = denoms[index]
    Explore all possible paths of denomiations
        Iterate through all denominations and compute remaining amount add it to ways.

2. Optimize this solution using memoization. Cache the result in a map where key is amount, index