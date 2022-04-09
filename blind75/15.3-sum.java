import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int i=0;
        int j = i + 1;
        int k = j + 1;
        // sort array [2,1,0,-1,-1,-4]
        Arrays.sort(nums);
        while(i<j<k) {
            if(nums[i] + nums[j] + nums[k] < 0) {
                
            }
        }
    }
}
// @lc code=end

