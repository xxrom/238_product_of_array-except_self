from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        ans = [None] * len(nums)
        for i in range(0, len(nums)):
          sum *= nums[i]
          ans[i] = sum

        sum = 1
        for i  in range(len(nums) - 1, -1, -1):
          if i != 0:
            ans[i] = sum * ans[i - 1]
            sum *= nums[i]
          else:
            ans[i] = sum


        # OLD VERSION WITH upDown array
        # and downUp array (multiplied one by one)
        # ans = []
        # for i in range(len(nums)):
        #   a = 1 if i == 0 else upDown[i - 1]
        #   b = 1 if i == len(nums) -1 else downUp[i + 1]
        #   ans.append(a*b)

        return ans



my = Solution()
n =  [1,2,3,4]
ans = my.productExceptSelf(n)
print("ans", ans)

# THIS SHOULD WORK =)
# [1,2,3,4] => [24, 12, 8, 6]
#     up-down   down-up
# 0 - 1         24
# 1 - 2         24
# 3 - 6         12
# 4 - 24        4

# x[i] = UD[i - 1] * DU[i + 1]
# It works, but too slow and a lot of memory usage 128ms (50%) / 20.8mb (6%)

#! New version with one array and two full cycle works much faster and less memory usage

# Runtime: 112 ms, faster than 98.13% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.5 MB, less than 82.00% of Python3 online submissions for Product of Array Except Self.