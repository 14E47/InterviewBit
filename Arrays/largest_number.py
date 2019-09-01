class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        n = len(A)
        mx = max(A)
        mn = min(A)

        A = sorted(list(A), key=lambda x: (int(str(x)[0]), int(str(x)[1])), reverse=True)
        # print(A)
        number = ''
        # for i in A:
        #     if len(number)==0:
        #         number = str(i)
        #     else:
        #         if int(str(i)+number) > int(number+str(i)):
        #             number = str(i) + number
        #         elif int(str(i)+number) < int(number+str(i)):
        #             number += str(i)
        #         elif int(str(i)+number) == int(number+str(i)):
        #             if int(number) != int(str(i)+number):
        #                 number += str(i)

        return number

def compare(x,y):


A = (3, 30, 34, 5, 9,30)
# A = (100, 10, 1000, 10)
# A = (5,)
# A = [ 0, 0, 0, 0, 0 ]
# A = [ 9, 99, 999, 9999, 9998 ]
# A = [ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]

print(Solution().largestNumber(A))

