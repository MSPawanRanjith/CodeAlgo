#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left <= right):
            pivot: int = int((left+right)/2)
            if(nums[pivot] == target):
                return pivot
            if(target > nums[pivot]):
                left = pivot + 1
            else:
                right = pivot - 1
        return -1


# @lc code=end
# Solution().search([-1, 0, 3, 5, 9, 12], 9)
