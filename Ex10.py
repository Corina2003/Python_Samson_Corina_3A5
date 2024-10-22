def combine_lists(*lists):
    max_length = max(len(lst) for lst in lists)

    result = []

    for i in range(max_length):
        tuple_elements = []
        for lst in lists:
            if i < len(lst):
                tuple_elements.append(lst[i])
            else:
                tuple_elements.append(None)
        result.append(tuple_elements)

    return result


result = combine_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c", "d"])
print(result)
