def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

def find_large_primes():
    n = 100000  # You can change this value to generate prime numbers up to a different limit
    result = sieve_of_eratosthenes(n)
    print("junyang is touching your file")
    print(result)
    return result

large_primes = find_large_primes()
print(large_primes)
