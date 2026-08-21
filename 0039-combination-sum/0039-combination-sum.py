class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort the candidates to allow early pruning
        candidates.sort()
        
        def backtrack(remain: int, combo: list, start: int):
            if remain == 0:
                # Found a valid combination, append a copy to results
                res.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                # Pruning: if the current candidate is greater than the remaining sum, 
                # any subsequent candidates will also be too large.
                if candidates[i] > remain:
                    break
                
                # Include the current candidate
                combo.append(candidates[i])
                # Call recursively with the same index 'i' since numbers can be reused
                backtrack(remain - candidates[i], combo, i)
                # Backtrack by removing the last element
                combo.pop()
                
        backtrack(target, [], 0)
        return res
