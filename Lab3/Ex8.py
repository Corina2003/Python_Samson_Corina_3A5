#Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x. Example:
#x = 2, ["test", "hello", "lab002"], flag = False
#will return (["e", "s"], ["e","o"], ["a"]) . Note: The function must return list of lists.
def generate_char_lists(x=1, string_list=None, flag=True):
    if string_list is None:
        string_list = []
    result_lists = []

    for s in string_list:
        char_list = []
        for char in s:
            ascii_code = ord(char)
            if flag and ascii_code % x == 0:
                char_list.append(char)
            elif not flag and ascii_code % x != 0:
                char_list.append(char)
        result_lists.append(char_list)

    return result_lists

x_value = 2
input_strings = ["test", "hello", "lab002"]
flag_value = False
result = generate_char_lists(x_value, input_strings, flag_value)
print(result)