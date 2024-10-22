#Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a, b):
    intersected = [value for value in a if value in b]
    reunited = a.copy()
    for value in b:
        if value not in reunited:
            reunited.append(value)
    a_minus_b = [value for value in a if value not in b]
    b_minus_a = [value for value in b if value not in a]

    return (intersected, reunited, a_minus_b, b_minus_a)


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = list_operations(list_a, list_b)
print(result)
