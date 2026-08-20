class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return an empty list immediately if the input string is empty
        if not digits:
            return []
            
        # Map digits to their corresponding keypad letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        # Helper function for backtracking
        def backtrack(index: int, current_path: list):
            # Base case: if the current combination length equals the input length
            if index == len(digits):
                combinations.append("".join(current_path))
                return
            
            # Get the letters mapped to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Explore each letter option
            for letter in possible_letters:
                current_path.append(letter)       # Choose
                backtrack(index + 1, current_path) # Explore next digit
                current_path.pop()                # Unchoose (backtrack)
                
        # Kick off the recursive exploration starting at index 0
        backtrack(0, [])
        return combinations
