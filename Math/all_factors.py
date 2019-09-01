class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = [1,]
        if A == 1:
            return factors
        for i in range(2, int(A**0.5)+1):
            if A%i == 0:
                factors.append(i)
                if A//i != i:
                    factors.append(A//i)
        factors.append(A)
        factors.sort()
        return factors

A = 82944
print(Solution().allFactors(A))
