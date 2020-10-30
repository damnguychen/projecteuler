"""
return median of each sliding window
leetcode 480: https://leetcode.com/problems/sliding-window-median/
"""

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        
        result = []
        
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            sorted_window = sorted(window)
            
            if k % 2 == 0:
                result.append((sorted_window[int(k/2 - 1)] + sorted_window[int(k/2)]) / 2)
                
            else:
                result.append(sorted_window[k//2])
                
        return result