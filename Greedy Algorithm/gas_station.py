class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):

        n = len(A)
        gas_available = sum(A)
        gas_required = sum(B)

        if gas_available < gas_required:
            return -1

        

        for i in range(n):
