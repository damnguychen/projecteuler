""" Problem
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

""" Idea
set up a mapping dictionary
if open bracket: append into a stack list
if close bracket:
	if map dictionary != stack.pop() or stack == []:
		False

return stack == []    # in case not closed brackets
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        map_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char in map_dict.values():
                stack.append(char)
                
            elif char in map_dict.keys():
                if stack == [] or map_dict[char] != stack.pop():
                    return False
            
        return stack == []