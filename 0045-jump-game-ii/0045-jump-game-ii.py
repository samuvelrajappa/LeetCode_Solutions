class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the array has only 1 element, no jumps are needed
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Traverse the array except for the last element
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from current position
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Proactive check: if we can already reach or exceed the last index
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
