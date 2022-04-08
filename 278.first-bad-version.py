#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        first_ver = 0
        last_ver = n-1
        bad_version = 0
        while(first_ver <= last_ver):
            pivot = int((first_ver + last_ver)/2)
            ver = pivot + 1
            if(isBadVersion(ver) == True):
                bad_version = ver
                last_ver = pivot - 1
                if(bad_version > pivot):
                    bad_version = pivot + 1
            else:
                first_ver = pivot + 1
        return bad_version

# @lc code=end

def isBadVersion(n):
    return True if n >= 1 else False

# print(Solution().firstBadVersion(5))
