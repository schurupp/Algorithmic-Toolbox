from sys import stdin

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def minimum_coins(m, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, m + 1):
        answer = None
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            answer = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return answer

if __name__ == '__main__':
    m, *coins = list(map(int, stdin.read().split()))
    print(minimum_coins(m, coins))