## Day 12 - Section 12: Beginner - Prime Number Checker

def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False  # 1 and numbers less than 1 are not prime
    if num == 2:
        return True  # 2 is the only even prime number
    if num % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for factors from 3 to the square root of num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False  # Found a divisor, so not prime

    return True  # No divisors found, so it's prime


# Example usage
print(is_prime(73))  # Output: True
print(is_prime(75))  # Output: False


