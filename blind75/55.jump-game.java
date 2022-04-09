/*
 * @lc app=leetcode id=55 lang=java
 *
 * Need to try this again in DP
 * this greedy approach seems good, but, need to think from backword approach
 * 
 * [55] Jump Game
 */

// @lc code=start
class Solution {
    public boolean canJump(int[] nums) {
        int post = nums.length - 1;
        for (int i=nums.length-1; i>=0; i--) {
            if(i + nums[i] >= post) {
                post = i;
            }
        }
        return(post == 0);
    }
}
// @lc code=end
