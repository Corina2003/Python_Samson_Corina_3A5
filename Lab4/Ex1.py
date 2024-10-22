#Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a, b):
    a_set = set(a)
    b_set = set(b)

    intersected = a_set.intersection(b_set)
    reunited = a_set.union(b_set)
    a_minus_b = a_set.difference(b_set)
    b_minus_a = b_set.difference(a_set)

    return (intersected, reunited, a_minus_b, b_minus_a)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = list_operations(list_a, list_b)
print(result)