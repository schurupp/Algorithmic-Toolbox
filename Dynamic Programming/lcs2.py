def lcs2(first_sequence, second_sequence):
    m, n = len(first_sequence), len(second_sequence)

    # Initialize a 2D array to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
