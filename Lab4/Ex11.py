#Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values. Ex:

#my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
def count_args(*args, **key_word_args):
    values = set(key_word_args.values())
    count = sum(1 for arg in args if arg in values)
    return count


result = count_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)