# Asked in Google


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = 0
        max_ranges = []

        current_sum = 0
        current_ranges = []

        for i in range(len(A)):

            if A[i] >= 0:
                current_sum += A[i]
                current_ranges.append(A[i])
            else:
                # print(current_sum, current_ranges)
                if max_sum < current_sum:
                    max_sum = current_sum
                    max_ranges = current_ranges
                if max_sum == current_sum:
                    if len(max_ranges) < len(current_ranges):
                        max_ranges = current_ranges

                current_sum = 0
                current_ranges = []

        if max_sum < current_sum:
            max_ranges = current_ranges
            max_sum = current_sum
        if max_sum == current_sum:
            if len(max_ranges) < len(current_ranges):
                max_ranges = current_ranges

        # print(max_sum, max_ranges, current_sum, current_ranges)
        if max_sum == 0:
            if current_sum == 0:
                return max_ranges
            return A
        else:
            return max_ranges


A = [1, 2, 4,1, -7, 1,2,2, 3,-8, 2,2,2,2]
A = [ 1477171087 ]
A = [ 39194, 51295, 33419, 63443, 68706, 26593, 31226 ]
A = [ -1, -1, -1, -1, -1 ]
A = [3,5, -7, 3,2, 3,-8, 4,2,1,1]
A = []
A = [ 0, 0, -1, 0 ]
A = [ -81293, -4101, 58248, 82332, 98765, 59002, 20719, 82437 ]

c = Solution().maxset(A)
print(c)
