class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, visited):
            # Base case: full permutation found
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    
                    # Recursively build remaining slots
                    backtrack(path, visited)
                    
                    # Backtrack to try other paths
                    path.pop()
                    visited.remove(num)
                    
        backtrack([], set())
        return res
