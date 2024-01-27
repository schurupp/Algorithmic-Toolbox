from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    i = 0
    j = 0
    while len(first_sequence) > 0:
        if max(first_sequence) * max(second_sequence) > 0:
            max_product += max(first_sequence)*max(second_sequence)
            first_sequence.remove(max(first_sequence))
            second_sequence.remove(max(second_sequence))
        elif max(first_sequence) * max(second_sequence) < 0:
            if min(first_sequence) * min(second_sequence) > 0:
                max_product += min(first_sequence)*min(second_sequence)
                first_sequence.remove(min(first_sequence))
                second_sequence.remove(min(second_sequence))
            else:
                max_product += max(first_sequence)*max(second_sequence)
                first_sequence.remove(max(first_sequence))
                second_sequence.remove(max(second_sequence))
        else:
            if max(first_sequence) == 0:
                max_product += max(first_sequence)*min(second_sequence)
                first_sequence.remove(max(first_sequence))
                second_sequence.remove(min(second_sequence))
            else:
                max_product += min(first_sequence)*max(second_sequence)
                first_sequence.remove(min(first_sequence))
                second_sequence.remove(max(second_sequence))
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
