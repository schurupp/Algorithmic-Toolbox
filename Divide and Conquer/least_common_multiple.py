import sys

def greatest_common_divisor(first, second):
    if second == 0:
        return first
    else:
        return greatest_common_divisor(second, first % second)

def least_common_multiple(first,second):
    num = greatest_common_divisor(first, second)
    multiplier = int(second / num)
    return first * multiplier

def main():
    # For array input
    arr = [int(x) for x in input().split()]
    first = arr[0]
    second = arr[1]
    testreturn = least_common_multiple(first,second)
    print(testreturn)

main()