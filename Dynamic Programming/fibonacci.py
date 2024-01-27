import sys

FibArray = [0, 1]
def fibonacci(n):
    if n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

def main():
    n = int(input())
    testreturn = fibonacci(n)
    print(testreturn)

main()