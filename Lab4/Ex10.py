#Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described. Ex:
def loop(mapping):
    visited = set()
    result = []
    current_key = "start"

    while current_key not in visited:
        visited.add(current_key)
        next_value = mapping[current_key]

        if next_value in visited:
            break

        result.append(next_value)
        current_key = next_value

    return result


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)
