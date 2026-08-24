class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < s_len:
            # Case 1: Characters match or pattern has '?'
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            
            # Case 2: Pattern has '*' -> Record position and try matching 0 characters first
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            
            # Case 3: Current match fails but a previous '*' was encountered -> Backtrack
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            
            # Case 4: No match and no previous '*' to look back to
            else:
                return False
        
        # Check for remaining trailing '*' characters in the pattern
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == p_len
