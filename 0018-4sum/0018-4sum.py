class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Sort the array to efficiently use two pointers and skip duplicates
        nums.sort()
        return self.kSum(nums, target, k=4, start=0)

    def kSum(self, nums: list[int], target: int, k: int, start: int) -> list[list[int]]:
        res = []
        
        # Base case checking: if we ran out of numbers, or remaining min possible sum 
        # is greater than target, or remaining max possible sum is less than target.
        if start == len(nums) or nums[start] * k > target or nums[-1] * k < target:
            return res
        
        # When k == 2, solve it using the classic Two Sum II (Two Pointers) approach
        if k == 2:
            return self.twoSum(nums, target, start)
        
        # For k > 2, recursively break it down into a (k-1)Sum problem
        for i in range(start, len(nums)):
            # Skip duplicate elements to guarantee unique quadruplets
            if i > start and nums[i] == nums[i - 1]:
                continue
                
            # Recursively call kSum with k - 1 and updated target
            for subset in self.kSum(nums, target - nums[i], k - 1, i + 1):
                res.append([nums[i]] + subset)
                
        return res

    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        res = []
        low = start
        high = len(nums) - 1
        
        while low < high:
            curr_sum = nums[low] + nums[high]
            
            if curr_sum < target:
                low += 1
            elif curr_sum > target:
                high -= 1
            else:
                res.append([nums[low], nums[high]])
                low += 1
                high -= 1
                # Skip duplicate elements for the left pointer
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                    
        return res
