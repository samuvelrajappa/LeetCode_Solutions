class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Store the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits using string manipulation
        reversed_x = int(str(x)[::-1]) * sign
        
        # Check for 32-bit overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
            
        return reversed_x
