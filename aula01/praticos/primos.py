def is_prime(number: int) -> bool:

    i = number
    divisors = []
    
    while i >= 1:
        if number%i == 0:
            divisors.append(i)

        i -= 1
        
    
    if len(divisors) > 2:
        return False

    return True

def is_prime_recursive(prime: int, divisor = 2) -> bool:

    if prime < 2:
        return False
    
    if divisor == prime:
        return True
    
    if prime%divisor == 0:
        return False
    
    return is_prime_recursive(prime, divisor+1)


if __name__ == "__main__":

    print(is_prime(10))
    print(is_prime_recursive(15))