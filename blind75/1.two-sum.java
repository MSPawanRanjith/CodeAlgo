import java.util.HashMap;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapping = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            if(mapping.containsKey(nums[i])){
                return new int[] {i, mapping.get(nums[i])};
            }
            mapping.put(target - nums[i], i);
        }
        return new int[] {};
    }
}
// @lc code=end

