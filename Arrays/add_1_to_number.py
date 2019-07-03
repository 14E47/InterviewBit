class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = int(''.join([str(i) for i in A])) + 1
        return [i for i in str(s)]