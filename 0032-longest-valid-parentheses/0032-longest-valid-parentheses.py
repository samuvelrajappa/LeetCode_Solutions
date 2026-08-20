class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack to store indices of parentheses
        # Initialized with -1 to serve as a base boundary for valid substrings
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the opening parenthesis
                stack.append(i)
            else:
                # Pop the top index when encountering a closing parenthesis
                stack.pop()
                
                if not stack:
                    # If empty, the current closing parenthesis is unmatched.
                    # Push its index to serve as the new baseline boundary.
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
