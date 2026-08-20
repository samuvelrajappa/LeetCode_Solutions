class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        is_negative = (dividend < 0) != (divisor < 0)
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1
            
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1
            
            dvd -= temp_dvs
            quotient += multiple
            
        return -quotient if is_negative else quotient
