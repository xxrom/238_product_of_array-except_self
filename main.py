from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print('hello')



my = Solution()
n =  [1,2,3,4]
ans = my.productExceptSelf(n)
print("ans", ans)




#          24
#    2           12
# 1     2     3     4


# x * y * z * m * n


# THIS SHOULD WORK =)
# [1,2,3,4]
#     up-down   down-up
# 0 - 1         24
# 1 - 2         24
# 3 - 6         12
# 4 - 24        4

# x[i] = UD[i - 1] * DU[i + 1]
