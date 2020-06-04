"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Brute force: two pointers
# time complexity: O(n^2)
# space complexity: O(1)

# Better: hash numbers into a dictionary: {key-value pair is number: index}
# time complexity: O(n)
# space complexity: O(n)

class Solution(object):
	def twoSum_bruteforce(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtyp
        """

        i = 0
        
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                else:
                    j = j + 1
            i = i + 1


    def twoSum_hash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        y_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in my_dict:
                my_dict[nums[i]] = i
            
            else:
                return [my_dict[target - nums[i]], i]