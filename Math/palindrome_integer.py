class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A == 0:
            return 1
        if A > 0:
            if A%10 == A:
                return 1
            else:
                x = A
                reverse = 0
                while A != 0:
                    reverse = reverse*10 + A%10
                    A //= 10

                if x == reverse:
                    return 1
                return 0
        else:
            return 0

A = 2147447412
print(Solution().isPalindrome(A))