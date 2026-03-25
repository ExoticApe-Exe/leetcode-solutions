# LeetCode #1 - Two Sum
# Topic: Arrays, HashMap
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
