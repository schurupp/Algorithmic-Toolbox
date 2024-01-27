def majority_element_divide_and_conquer(elements):
    def find_majority_element(left, right):
        if left == right:
            return elements[left]

        mid = (left + right) // 2
        left_majority = find_majority_element(left, mid)
        right_majority = find_majority_element(mid + 1, right)

        if left_majority == right_majority:
            return left_majority

        left_count = sum(1 for i in range(left, right + 1) if elements[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if elements[i] == right_majority)

        return left_majority if left_count > right_count else right_majority

    majority_candidate = find_majority_element(0, len(elements) - 1)
    
    count_majority = elements.count(majority_candidate)
    if count_majority > len(elements) // 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_divide_and_conquer(input_elements))
