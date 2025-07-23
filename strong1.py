import math

def is_strong_number(n):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits is equal to the number itself.
    """
    if n < 0:
        return False
    
    original_n = n
    sum_of_factorials = 0
    
    while n > 0:
        digit = n % 10
        sum_of_factorials += math.factorial(digit)
        n //= 10
        
    return sum_of_factorials == original_n

def find_strong_numbers_in_range(start, end):
    """
    Finds and prints all strong numbers within a specified range (inclusive).
    """
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers

# Define the range
start_range = 1
end_range = 5000

# Find strong numbers in the specified range
strong_nums_found = find_strong_numbers_in_range(start_range, end_range)

# Print the results
print(f"Strong numbers between {start_range} and {end_range}:")
if strong_nums_found:
    print(strong_nums_found)
else:
    print("No strong numbers found in this range.")