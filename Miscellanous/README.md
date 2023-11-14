# Problem statement
Given an array of integers, find out the number ot distinct triplets whose sum (arr[i]+arr[j]+arr[k]) be is divisible by a given number d and (i < j < k). 

```
Input:
arr = [2, 3, 1, 6]
d = 3
Output: 2
```

# Brute force 
1. Try out all the combinations of i,j,k count the values whose sum is divisible by d.
Time complexity: O(N^3)

# optimal solution 
Let A be an array of numbers of length N:

A = [1,2,3,4,5,6,7,8]
Let D be the divider

D = 4
It is possible to reduce complexity O(N^2) with an extra space dictionary that saves you iterating through the array for each pair (a[i],a[j]). The helper dictionary will be built before iterating through the pairs (i,j) with the count of A[k] % D = X. So for any pair A[i], A[j] you can tell how many matching A[k] exist by fetching from a dictionary rather than a loop.

Below is a python implementation that demonstrates the solution

T = 0 # Total possibilities
H = {} # counts all possible (A[k])%D = Key from index k

for k in range(2, len(A)):
  key = A[k]%D
  H[key] = H.get(key,0) + 1

for j in range(1, len(A)):
  if j >= 2:
    H[A[j]%D] -= 1 # when j increments it reduces options for A[k]
  for i in range(j):
    matching_val = (D - (A[i]+A[j]) % D ) % D
    to_add = H.get(matching_val, 0)
    T += to_add

print(T)