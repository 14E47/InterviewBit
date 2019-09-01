class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = list(A)
        A.sort()
        gap = 0
        for i in range(1,len(A)):
            diff = A[i] - A[i-1]
            if diff > gap:
                gap = diff
        return gap


# Input : [1, 10, 5]
# Output : 5
A = (1, 10, 5)

c = Solution()
print(c.maximumGap(A))