/*
 * @lc app=leetcode id=11 lang=java
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        
        int maxArea = 0;
        int i = 0;
        int j = height.length - 1;
        
        while(i < j) {
            int area =  Math.min(height[i], height[j]) * ((j+1) - (i+1));
            maxArea = area > maxArea ? area : maxArea;
            if(height[i] > height[j]) {
                j--;
            } else {
                i++;   
            }
        }
        
        return maxArea;
        
        
        // Brute force logic
        // List areaList = new ArrayList();
        // int maxArea = 0;
        // for(int i=0; i<height.length; i++) {
        //    for(int j=i+1; j<height.length; j++) {
        //        int area = Math.min(height[i], height[j]) * ((j+1) - (i+1));
        //        if(area > maxArea) {
        //            maxArea = area;
        //        }
        //    }
        // }
        // return maxArea;
    }
}
// @lc code=end

