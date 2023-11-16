def makeChange(amount, denoms, index):
    if index >= len(denoms) - 1: # last denom
        return 1
    denomAmount = denoms[index]
    ways = 0
    for i in range(0, amount):
        amountRemaining = amount - i * denomAmount
        i = i * denomAmount
        ways += makeChange(amountRemaining, denoms, index + 1)
    return ways

def makeChangeMemo(amount, denoms, index, memo):
    if (amount, index) in memo:
        return memo[(amount, index)]
    if index >= len(denoms) - 1: # last denom
        return 1
    denomAmount = denoms[index]
    ways = 0
    for i in range(0, amount):
        amountRemaining = amount - i * denomAmount
        i = i * denomAmount
        ways += makeChange(amountRemaining, denoms, index + 1)
    memo[(amount, index)] = ways
    return memo[(amount, index)]

if __name__ == "__main__":
    n = int(input())
    denoms = [25, 10, 5, 1]
    
    # recursion
    ways = makeChange(n, denoms, 0)
    print("[Recursion] Number of ways n can be formed using denominations: ", ways)

    # memoization
    ways_memo = makeChangeMemo(n, denoms, 0, {})
    print("[Memoization] Number of ways n can be formed using denominations: ", ways_memo)