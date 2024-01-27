def longest_palindrome(s):
    a = list(s)
    procd = list()
    oddcount = 0
    count = 0
    for char in a:
        if char not in procd:
            procd.append(char)
            if a.count(char) % 2 == 0:
                count += a.count(char)
            elif a.count(char) > oddcount:
                    if oddcount != 0:
                         count += oddcount - 1
                    oddcount = a.count(char)
            else:
                 count += a.count(char) - 1
    count += oddcount
    return count

def main():
    s = input()
    testreturn = longest_palindrome(s)
    print(testreturn)

main()