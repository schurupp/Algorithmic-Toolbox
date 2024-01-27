def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    n = len(dataset)
    digits = (n + 1) // 2
    dp_max = [[float('-inf')] * digits for _ in range(digits)]
    dp_min = [[float('inf')] * digits for _ in range(digits)]

    for i in range(digits):
        dp_max[i][i] = int(dataset[2 * i])
        dp_min[i][i] = int(dataset[2 * i])

    for len_subexpr in range(1, digits):
        for i in range(digits - len_subexpr):
            j = i + len_subexpr
            for k in range(i, j):
                op = dataset[2 * k + 1]
                dp_max[i][j] = max(dp_max[i][j], evaluate(dp_max[i][k], dp_max[k + 1][j], op),
                                  evaluate(dp_max[i][k], dp_min[k + 1][j], op),
                                  evaluate(dp_min[i][k], dp_max[k + 1][j], op),
                                  evaluate(dp_min[i][k], dp_min[k + 1][j], op))
                dp_min[i][j] = min(dp_min[i][j], evaluate(dp_max[i][k], dp_max[k + 1][j], op),
                                  evaluate(dp_max[i][k], dp_min[k + 1][j], op),
                                  evaluate(dp_min[i][k], dp_max[k + 1][j], op),
                                  evaluate(dp_min[i][k], dp_min[k + 1][j], op))

    return dp_max[0][-1]

if __name__ == "__main__":
    print(maximum_value(input()))
