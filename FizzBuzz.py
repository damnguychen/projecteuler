"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            element = ''
            
            if (i + 1) % 3 == 0:
                element += 'Fizz'
                
            if (i + 1) % 5 == 0:
                element += 'Buzz'
                
            if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
                element = str(i + 1)
                
            result.append(element)
            
        return result