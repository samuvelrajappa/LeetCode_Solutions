class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to bring duplicates next to each other
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: if the current number is the same as the previous one
                # and the previous one hasn't been used in this path branch yet
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                # Backtrack
                path.pop()
                used[i] = False
                
        backtrack([])
        return res
