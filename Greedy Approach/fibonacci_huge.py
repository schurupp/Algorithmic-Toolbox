def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    pisano = pisano_period(m)
    if n % pisano == 0:
        return previous % m
    elif n % pisano == 1:
        return current % m
    else:
            for _ in range(n % pisano - 1):
                previous, current = current, previous + current

    return current % m

def pisano_period(m):
    a, b = 0, 1
    period = 1

    for i in range(m * m):
        a, b = b, (a + b) % m

        if a == 0 and b == 1:
            period = i + 1
            break

    return period


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
