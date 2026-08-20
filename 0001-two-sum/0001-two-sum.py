class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store numbers and their corresponding indices
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the complement value needed to reach the target
            complement = target - num
            
            # If the complement exists in the map, a valid pair is found
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the current number and its index in the map
            num_to_index[num] = index
