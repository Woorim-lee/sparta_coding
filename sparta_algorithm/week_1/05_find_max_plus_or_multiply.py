input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array: # for문 한개 뿐이니, 시간복잡도는 O(N) 이구나!
        if number <= 1 or multiply_sum == 0:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)