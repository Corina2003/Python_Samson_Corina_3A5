#Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def count_and_max(numbers):
    palindrome_count = 0
    max = None

    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if max is None or number > max:
                max = number

    return palindrome_count, max

number_list = [121, 12321, 456, 101, 1331]
count, max = count_and_max(number_list)
result = (count, max)
print(result)