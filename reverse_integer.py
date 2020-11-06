class Solution:
    def reverse(self, x: int) -> int:

        output = ''
        target_str = str(x)
        
        if target_str[0] == '-':
            output = '-'
            target_str = target_str[1:]
            
        i = -1
        while i >= -len(target_str):
            output += target_str[i]
            i -= 1
            
        if int(output) > 2**31 -1 or int(output) < -2**31 - 1:
            return 0
        
        else:
            return int(output)