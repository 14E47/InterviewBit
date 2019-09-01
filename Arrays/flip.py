
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        if A == '1'*n:
            return []
        elif A == '0'*n:
            return [1,n]
        else:
            array = []
            for i in A:
                if i == '0':
                    array.append(1)
                elif i == '1':
                    array.append(-1)
            sub_index = self.maxSubArraySum(array)

            return [sub_index[0]+1, sub_index[1]+1]

    def maxSubArraySum(self,a):
        n = len(a)
        maximum = 0
        current = 0

        start = 0
        end = 0
        s = 0

        for i in range(n):
            current += a[i]

            if maximum < current:
                maximum = current
                start = s
                end = i


            if current < 0:
                current = 0
                s = i+1

        return start,end

S = '010'
S = '111'
S = '000'
S = '101'
S = '11100'
S = '000011'
S = '010101'
c = Solution().flip(S)
print(c)
