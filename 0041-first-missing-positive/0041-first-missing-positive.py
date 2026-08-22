class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # In-place placement of elements to their correct index (x -> index x - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target position
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Find the first index that does not match the expected value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all numbers 1 to n are present
        return n + 1
