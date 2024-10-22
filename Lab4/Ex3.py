#Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def compare(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            if not compare(dict1[key], dict2[key]):
                return False
        return True

    if isinstance(dict1, (list, tuple)):
        if len(dict1) != len(dict2):
            return False
        for i in range(len(dict1)):
            if not compare(dict1[i], dict2[i]):
                return False
        return True

    if isinstance(dict1, set):
        return dict1 == dict2

    return dict1 == dict2

dict1 = {
    'a': 1,   #int
    'b': [2, 3],  #list
    'c': {'x': 4, 'y': 5},  #dict
    'd': (6, 7),   #tuple
    'e': {8, 9}   #set
}

dict2 = {
    'a': 1,
    'b': [2, 3],
    'c': {'x': 4, 'y': 5},
    'd': (6, 7),
    'e': {8, 9}
}

result = compare(dict1, dict2)
print(result)


