def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def Goldbach(n):
    """Returns a list of tuples (a, b) where a + b = n and both are prime."""
    pairs = []
    
    # We only check up to n // 2 to satisfy the condition a <= b
    for a in range(2, (n // 2) + 1):
        b = n - a
        
        # If both a and its complement b are prime, it's a valid Goldbach pair
        if is_prime(a) and is_prime(b):
            pairs.append((a, b))
            
    return pairs