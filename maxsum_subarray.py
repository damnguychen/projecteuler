"""
Return maximum sum among all subarray
leetcode 53: https://leetcode.com/problems/maximum-subarray/
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_sum = [nums[0]]
        max_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            local_sum.append(max(nums[i], local_sum[-1] + nums[i]))
            max_sum.append(max(local_sum[-1], local_sum[-2]))
            
        return max(max_sum)