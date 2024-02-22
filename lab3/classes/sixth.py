class PrimeFilter:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def filter_primes(self, numbers):
        return list(filter(self.is_prime, numbers))
    
"""
numbers = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_filter = PrimeFilter()
prime_numbers = prime_filter.filter_primes(numbers)
print(prime_numbers)
"""