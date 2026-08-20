class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        max_length = 0
        left = 0  # Left pointer of our sliding window
        
        # Iterate through the string with the right pointer
        for right, char in enumerate(s):
            # If the character is already in the window, shrink the window from the left
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the last seen index of the current character
            char_map[char] = right
            
            # Calculate and update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
