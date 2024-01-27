import sys

def test(a):
    return a

def main():
    # For number of elements
    n = int(input())
    # For array input
    arr = [int(x) for x in input().split()]

    testreturn = test(arr)
    print(testreturn)

main()