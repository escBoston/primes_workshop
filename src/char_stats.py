import numpy as np

class Char_stats():
    def __init__(self):
        self.count = 0
        self.primes = []

    def get_count(self):
        return self.count

    def set_count(self, c):
        self.count=c

    def get_prime_count(self):
        return len(self.primes)

    def add_prime(self, prime):
        self.primes.append(prime)

    def get_avg_prime(self):
        return np.mean(self.primes)

    def get_prime_percentage(self):
        return self.get_prime_count() / self.get_count() if self.get_count() > 0 else 0
