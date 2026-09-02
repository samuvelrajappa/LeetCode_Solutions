class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both maximums with the first element
        max_so_far = nums[0]
        current_max = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Decide whether to add the current number to the existing subarray 
            # or start a new subarray from the current number
            current_max = max(num, current_max + num)
            
            # Update the global maximum if the current subarray sum is larger
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far
