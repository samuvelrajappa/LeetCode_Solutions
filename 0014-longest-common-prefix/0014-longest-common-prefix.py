class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: empty input list
        if not strs:
            return ""
        
        # Iterate through characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Compare this character with the same index in all other strings
            for string in strs[1:]:
                # If index is out of bounds or characters do not match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
