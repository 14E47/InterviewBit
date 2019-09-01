class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):

        def is_prime(num):
            if num == 1:
                return 0
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return 0
            return 1

        for i in range(2,A+1):
            if is_prime(i):
                if is_prime(A-i):
                    return [i, A-i]

A = 16777214
print(Solution().primesum(A))