class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A == 0:
            return 0
        if A > 0:
            if A%10 == A:
                return A
            else:
                reverse = 0
                while A != 0:
                    reverse = reverse*10 + A%10
                    A //= 10
                if reverse > 2147483647:
                    return 0
                return reverse
        else:
            A = abs(A)
            if A%10 == A:
                return -A
            else:
                reverse = 0
                while A != 0:
                    reverse = reverse*10 + A%10
                    A //= 10
                if reverse < -2147483647:
                    return 0

                return -reverse

A = -321
print(Solution().reverse(A))