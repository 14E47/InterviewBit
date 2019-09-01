class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        duplicate = None
        dic = {}

        for i in A:

            if i in dic:
                duplicate = i
                break
            dic[i] = 1

        if duplicate is None:
            return -1
        else:
            return duplicate

A = ()

c = Solution().repeatedNumber(A)
print(c)