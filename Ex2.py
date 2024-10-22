#Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0:
            return False
        i += 3

    return True

def find_primes(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = find_primes(numbers)
print(prime_numbers)
