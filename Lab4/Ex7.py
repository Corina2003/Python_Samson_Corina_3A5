#Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. Ex:

def set_operations(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            key = f"{set_a} | {set_b}"
            result[key] = set_a | set_b

            key = f"{set_a} & {set_b}"
            result[key] = set_a & set_b

            key = f"{set_a} - {set_b}"
            result[key] = set_a - set_b

            key = f"{set_b} - {set_a}"
            result[key] = set_b - set_a

    return result


set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)

for key, value in result.items():
    print(f"'{key}': {value},")

