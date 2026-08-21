class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # Sort candidates to ensure duplicates are adjacent and allow pruning
        candidates.sort()
        
        def backtrack(start: int, current_target: int, path: List[int]):
            # Base case: if target is met, record the valid combination
            if current_target == 0:
                ans.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Early pruning: since array is sorted, subsequent elements will also exceed target
                if candidates[i] > current_target:
                    break
                
                # Skip duplicate elements at the same recursion level to avoid duplicate paths
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the current candidate
                path.append(candidates[i])
                # Recurse to the next index (each candidate can be used only once)
                backtrack(i + 1, current_target - candidates[i], path)
                # Backtrack to try other combinations
                path.pop()
                
        backtrack(0, target, [])
        return ans
