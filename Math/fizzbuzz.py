class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        out = []
        for i in range(1,A+1):
            if i%15 == 0:
                out.append('FizzBuzz')
            elif i%3 == 0:
                out.append('Fizz')
            elif i%5 == 0:
                out.append('Buzz')
            else:
                out.append(str(i))

        return out

A = 15
print(Solution().fizzBuzz(A))