class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        spiral = []
        r = len(A)
        c = len(A[0])

        count = 0
        while count != r*c:

            for i in range(1,r+1):
                for j in range(1,c+1):
                    # if i
                    print(i,j)
                    c += 1


A = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print(Solution().spiralOrder(A))