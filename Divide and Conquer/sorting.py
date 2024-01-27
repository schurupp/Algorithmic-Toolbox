from random import randint


def partition3(array, left, right):
    pivot_value = array[left]
    low, high = left, right
    i = left
    while i <= high:
        if array[i] < pivot_value:
            array[i], array[low] = array[low], array[i]
            low += 1
            i += 1
        elif array[i] > pivot_value:
            array[i], array[high] = array[high], array[i]
            high -= 1
        else:
            i += 1

    return low, high

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
