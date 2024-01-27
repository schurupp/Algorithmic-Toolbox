import sys

def max_pairwise_product(a):
    first = -sys.maxsize
    second = -sys.maxsize
    for num in a:
        if num >= first:
            second = first
            first = num
        elif num >= second:
            second = num
    return first * second

def main():
    # For number of elements
    n = int(input())
    # For array input
    arr = [int(x) for x in input().split()]

    max_product = max_pairwise_product(arr)
    print(max_product)

main()