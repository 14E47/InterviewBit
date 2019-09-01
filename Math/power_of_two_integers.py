class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        for i in range(2, int(A**0.5)+1):
            pow = 1
            while i**pow <= A:
                pow += 1
            if i**(pow-1) == A:
                return 1
        return 0



A = 90
print(Solution().isPower(A))