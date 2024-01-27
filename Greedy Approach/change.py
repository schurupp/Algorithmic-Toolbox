def change(money):
    count = 0
    while True:
        if money >= 10:
            money -= 10
            count += 1
        elif money >= 5:
            money -= 5
            count += 1
        elif money >= 1:
            money -= 1
            count += 1
        else:
            return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
