class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        answer = A[0]
        max_now = A[0]

        if len(A) == 1:
            return A[0]

        for i in range(len(A) - 1):
            max_now += A[i + 1]
            if max_now < A[i + 1]:
                max_now = A[i + 1]
            if answer < max_now:
                answer = max_now

        return answer
