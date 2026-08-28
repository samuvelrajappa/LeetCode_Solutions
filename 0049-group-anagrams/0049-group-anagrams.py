from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary where each key maps to a list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to form the key
            sorted_key = "".join(sorted(s))
            
            # Append the original string to its corresponding anagram group
            anagram_map[sorted_key].append(s)
            
        # Return all grouped anagrams as a list of lists
        return list(anagram_map.values())
