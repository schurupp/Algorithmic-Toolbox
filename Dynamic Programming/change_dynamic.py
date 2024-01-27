def change(money):
    coins = [4, 3, 1]
    n = len(coins)

    # Create a table to store the results of subproblems
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    # Fill the table using bottom-up dynamic programming
    for i in range(1, money + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])

    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
