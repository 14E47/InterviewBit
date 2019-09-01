class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A == 0:
            return '0'
        binary = ''
        while A != 0:
            binary += str(A%2)
            A //= 2

        return binary[::-1]

A = 6
print(Solution().findDigitsInBinary(A))