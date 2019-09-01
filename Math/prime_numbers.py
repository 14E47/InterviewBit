class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):

        def is_prime(num):
            if num == 1:
                return 0
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return 0
            return 1

        if A < 2:
            return []
        primes = [2,]
        for i in range(3,A+1,2):
            if is_prime(i) == 1:
                primes.append(i)
        return primes

A = 7
print(Solution().sieve(A))
