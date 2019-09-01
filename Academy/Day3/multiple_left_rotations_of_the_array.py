class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)

        if n == 1:
            return [A for i in range(m)]

        result = []
        for i in B:
            mod = i%n
            result.append(A[mod:] + A[:mod])
        return result

A = [1, 2, 3, 4, 5]
B = [2, 3, 24]
A = [ 6, 31, 33, 13, 82, 66, 9, 12, 69, 21,
      17, 2, 50, 69, 90, 71, 31, 1, 13, 70,
      94, 46, 89, 13, 55, 54, 67, 97, 28, 27,
      62, 34, 41, 18, 15, 35, 13, 84, 93, 27,
      89, 23, 6, 56, 94, 40, 54, 95, 47 ]
B = [ 88, 85, 98, 39, 66, 40, 30, 26, 51, 77, 62, 60, 92, 64, 53, 86, 24, 53, 85, 49, 57, 29, 32, 60, 75, 82, 17, 23, 67, 51, 23, 11, 70, 59 ]


print(Solution().solve(A,B))

