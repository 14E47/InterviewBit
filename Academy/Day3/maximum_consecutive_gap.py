class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        A = list(A)
        A.sort()

        max_distance = 0
        for i in range(1, n):
            max_distance = max(max_distance, A[i] - A[i - 1])
        return max_distance
