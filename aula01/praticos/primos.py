import random
import time

def is_prime(number: int) -> bool:

    i = 1

    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False

    return True

def is_prime_recursive(number: int, divisor = 2) -> bool:

    if number < 2:
        return False
    
    if divisor > int(number**0.5):
        return True
    
    if number%divisor == 0:
        return False
    
    return is_prime_recursive(number, divisor+1)

def get_random_vector(array_size: int, max_value: int) -> list:
    
    return [random.randint(1, max_value) for _ in range(array_size)]

def get_biggest_prime(vector: list) -> int:
    biggest_prime = 0

    for number in vector:
        if is_prime(number) and number > biggest_prime:
            biggest_prime = number

    return biggest_prime

def get_biggest_prime_recursive(vector: list) -> int:
    biggest_prime = 0

    for number in vector:
        if is_prime_recursive(number) and number > biggest_prime:
            biggest_prime = number
    return biggest_prime

if __name__ == "__main__":

    # Get random vector
    vector = get_random_vector(100000, 100000)

    # Get start time
    start = time.time()
    # Get prime numbers with interative method
    biggest_prime = get_biggest_prime(vector)
    # Get end time
    end = time.time()
    print(f"Biggest prime number using iterative method: {biggest_prime}, time: {end - start}")

    # Get start time
    start = time.time()
    # Get prime numbers with recursive method
    biggest_prime = get_biggest_prime_recursive(vector)
    # Get end time
    end = time.time()
    print(f"Biggest prime number using recursive method: {biggest_prime}, time: {end - start}")