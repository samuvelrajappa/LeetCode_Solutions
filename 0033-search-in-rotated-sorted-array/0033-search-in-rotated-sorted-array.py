class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            
            # Otherwise, the right half must be sorted
            else:
                # Check if the target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left
                    
        return -1  # Target not found
