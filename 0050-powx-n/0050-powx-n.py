class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents by taking the reciprocal of the base
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x
        
        while n > 0:
            # If the current power is odd, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product
            # Square the base product and half the remaining exponent
            current_product *= current_product
            n //= 2
            
        return result
