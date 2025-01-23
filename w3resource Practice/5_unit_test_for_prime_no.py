import unittest

def is_prime(num):
    if num<2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

class TestPrime(unittest.TestCase):
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
        for num in prime_numbers:
            self.assertTrue(is_prime(num), f"{num} is not a prime number")
    
    def test_non_prime_numbers(self):
        prime_numbers = [1, 4, 6, 9, 12, 10, 90]
        for num in prime_numbers:
            self.assertFalse(is_prime(num), f"{num} is incorrectly identified prime number")

if __name__ == "__main__":
    unittest.main()