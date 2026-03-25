// LeetCode #1 - Two Sum
// Topic: Arrays, HashMap
// Difficulty: Easy
// Time Complexity: O(n)
// Space Complexity: O(n)

// Example:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }

            map.put(nums[i], i);
        }

        return new int[]{};
    }
}
