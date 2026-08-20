class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            
        # For even length numbers, x == reverted_number
        # For odd length numbers, x == reverted_number // 10 (removes the middle digit)
        return x == reverted_number or x == reverted_number // 10
