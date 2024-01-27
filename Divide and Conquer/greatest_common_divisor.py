import sys

def greatest_common_divisor(first, second):
    if second == 0:
        return first
    else:
        return greatest_common_divisor(second, first % second)

def main():
    # For array input of 2 numbers
    arr = [int(x) for x in input().split()]
    first = arr[0]
    second = arr[1]
    gcd = greatest_common_divisor(first, second)
    print(gcd)

main()