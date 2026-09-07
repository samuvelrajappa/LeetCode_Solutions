class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Tracks the maximum index we can reach so far
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the max reachable index, we are stuck
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach
            max_reachable = max(max_reachable, i + jump)
            
            # Optimization: If we can already reach the last index, return True early
            if max_reachable >= len(nums) - 1:
                return True
                
        return True
