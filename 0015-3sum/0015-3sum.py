class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to easily handle duplicates and use two pointers
        nums.sort()
        
        for i in range(len(nums)):
            # If the current number is greater than 0, remaining numbers 
            # will also be greater than 0, so they cannot sum up to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Use two pointers for the remaining part of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicate elements for the second position
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
