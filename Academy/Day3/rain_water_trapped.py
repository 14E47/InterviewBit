class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        trapped = 0
        l_max = -1
        r_max = -1
        l = []
        r = []
        for i in range(1,n-1):
            l_max = max(l_max,A[i-1])
            l.append(l_max)
            r_max = max(r_max, A[-i])
            r.append(r_max)

        r = r[::-1]
        for i in range(1,n-1):
            w = min(l[i-1], r[i-1])
            if A[i] <= w:
                trapped += w - A[i]
        return trapped

A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
print(Solution().trap(A))
