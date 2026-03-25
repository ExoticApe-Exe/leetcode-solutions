# LeetCode #53 - Maximum Subarray
# Topic: Arrays, Dynamic Programming
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum
