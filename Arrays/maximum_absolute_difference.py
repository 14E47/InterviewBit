class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = -2147483648
        min1 = +2147483647
        max2 = -2147483648
        min2 = +2147483647

        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)

        return max(max1 - min1, max2 - min2)


A = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98]
A = [ 2, 2, 2]
A = [ 55, -8, 43, 52, 8, 59, -91, -79, -18, -94 ]

c  = Solution().maxArr(A)
print(c)
