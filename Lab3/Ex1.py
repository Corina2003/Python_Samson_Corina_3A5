#Write a function to return a list of the first n numbers in the Fibonacci string.
def generate_fibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

n = 10
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
