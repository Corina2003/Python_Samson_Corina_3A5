
def find_elements_appearing_x_times(x, *lists):
    frequency = {}

    for lst in lists:
        for item in lst:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

    result = [item for item, count in frequency.items() if count == x]

    return result


result = find_elements_appearing_x_times(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print(result)
