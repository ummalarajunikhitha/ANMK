def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If num is divisible by any number in this range, it's not prime.
    return True  # If no divisors are found, the number is prime.

print("Prime numbers between 1 and 100 are:")
for number in range(1, 101):
    if is_prime(number):
        print(number)