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

def is_prime_recursive(prime: int, test_number = 2) -> bool:

    if prime%test_number == 0:
        return False
    
    if test_number == prime:
        return False
    
    test_number+=1
    is_prime_recursive(prime, test_number)







if __name__ == "__main__":

    print(is_prime(10))