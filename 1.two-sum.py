#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(target == nums[i] + nums[j]):
                    return [i, j]
# @lc code=end

print(Solution().twoSum([2,7,11,15], 9))