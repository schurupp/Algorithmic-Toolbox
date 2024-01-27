from sys import stdin

def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])

    return dp[n][capacity]

if __name__ == '__main__':
    capacity, num_golds = map(int, input().split())
    gold_values = list(map(int, input().split()))
    assert len(gold_values) == num_golds

    print(maximum_gold(capacity, gold_values))
