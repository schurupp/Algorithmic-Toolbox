def assign_cookies(g, s):
        count = 0
        total = sum(s)
        quantity = len(s)
        for child in sorted(g):
            if total - child >= 0 and count < quantity:
                count += 1
                g.remove(child)
                total -= child
            else:
                return count
        return count

def main():
    a = [int(x) for x in input().split(" ")]
    g = [int(x) for x in list(str(a[0]))]
    s = [int(x) for x in list(str(a[1]))]

    testreturn = assign_cookies(g, s)
    print(testreturn)

main()