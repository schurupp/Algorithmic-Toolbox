from sys import stdin

def partition3(values):
    total_sum = sum(values)

    if total_sum % 3 != 0:
        return 0
    
    target_sum = total_sum // 3
    n = len(values)

    dp = [[[False for _ in range(target_sum + 1)] for _ in range(n + 1)] for _ in range(4)]

    for i in range(n + 1):
        dp[0][i][0] = True

    for k in range(1, 4):
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                dp[k][i][j] = dp[k][i - 1][j]
                if j >= values[i - 1]:
                    dp[k][i][j] = dp[k][i][j] or dp[k - 1][i - 1][j - values[i - 1]]

    return 1 if dp[3][n][target_sum] else 0

if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
