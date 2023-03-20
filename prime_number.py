"""Prime number"""

def prime_number(num: int) -> bool:
    """
    Define is argument a prime numder. If true, returm True, else:
    return False.
    """
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1 
    return True


def factorize_number(num: int) -> None:
    """
    factorize a number. Print multipliers.
    """
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            print(divisor)
            num //= divisor
        else:
            divisor += 1


print(prime_number(557))
factorize_number(452841)
