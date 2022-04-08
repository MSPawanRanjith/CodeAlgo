#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return pivot+1 if(nums[pivot] < target)else pivot

# @lc code=end
# Repo to store my leet-code solution, these are not my perfect code, I am just trying to bring my algo and ds skills to its peak.

# print(Solution().searchInsert([1, 3, 5, 6], 7))

# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
#         large_num = str(A[0])
#         for i in range(0, len(A)-1):
#             large_num = sortLarge(str(large_num), str(A[i+1]))
#         print(large_num)
#         return large_num

# def sortLarge(a, b):
#     print (a+b, type(a+b))
#     print (int(a+b), type(int(a+b)))
#     return (a + b) if int(a+b) > int(b+a) else (b+a)

# print(Solution().largestNumber([3, 30, 34, 5, 9]))