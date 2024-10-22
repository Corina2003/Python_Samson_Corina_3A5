#Write a function that receives as a parameter a list and returns a tuple (a, b), a representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).
def count(lst):
    unique_elements = set(lst)
    duplicate_elements = len(lst) - len(unique_elements)
    return (len(unique_elements), duplicate_elements)

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
result = count(my_list)
print(result)
