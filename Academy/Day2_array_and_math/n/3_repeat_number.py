class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        n3 = n // 3

        dic = {}
        for i in A:
            try:
                dic[i] += 1
            except:
                dic[i] = 1

        for i in list(dic):
            if dic[i] > n3:
                return i
        return -1

A = (1,2,3,1,1)
print(Solution().repeatedNumber(A))


