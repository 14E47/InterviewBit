class Solution:

    def hotel(self, arrive, depart, K):

        arrive.sort()
        depart.sort()

        guests = 0

        for i in range(len(arrive)):
            guests += 1

            while arrive[i] >= depart[0]:
                depart.pop(0)
                guests -= 1
                if len(depart) == 0:
                    break

            if guests > K:
                return 0

            print(arrive)
            print(depart, "\n")

        return 1


A = [ 40, 18 ]
B = [ 40, 43 ]
C = 1

A = [ 1, 2, 3 ]
B = [ 2, 3, 4 ]
C = 1

A = [1, 3, 5]
B = [2,6,8]
C = 1

A = [ 9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27 ]
B = [ 32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ]
C = 16

c = Solution().hotel(A, B, C)
print(c)

# initial approach - Time limit exceeded

# def hotel(self, arrive, depart, K):
#     AD = sorted(list(zip(arrive, depart)))
#     D = []
#     count = 0
#
#     for i, j in AD:
#         if i != j:
#             count += 1
#             gone = len([k for k in D if k <= i])
#             D.append(j)
#
#             if count - gone > K:
#                 return 0
#
#     return 1