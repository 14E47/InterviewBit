class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        if A == '1'*n:
            return []
        elif A == '0'*n:
            return [1,2]
        else:
            count = 0
            lr = [0,0]
            for i in range(n):
                for j in range(i,n):
                    zeroes = A[i:j+1].count('0')
                    ones = len(A[i:j+1])-zeroes
                    if count < zeroes-ones:
                        count = zeroes-ones
                        lr = [i+1,j+1]
            return lr



S = '010'
S = '111'
S = '000'
S = '101'
S = '11100'
S = '000011'
S = '010101'
c = Solution().flip(S)
print(c)
