def lcs3(first_sequence, second_sequence, third_sequence):
    p, q, r = len(first_sequence), len(second_sequence), len(third_sequence)

    # Initialize a 3D array to store the lengths of LCS
    dp = [[[0] * (r + 1) for _ in range(q + 1)] for _ in range(p + 1)]

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, p + 1):
        for j in range(1, q + 1):
            for k in range(1, r + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[p][q][r]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
