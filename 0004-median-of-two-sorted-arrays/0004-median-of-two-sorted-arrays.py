class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = total_left - partition1
            
            # Edge cases: handle empty partitions with infinity boundaries
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have partitioned the arrays correctly
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Odd combined length: return the maximum element of the left side
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # Even combined length: return average of middle elements
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            # Partition1 is too far right; move it left
            elif max_left1 > min_right2:
                high = partition1 - 1
            # Partition1 is too far left; move it right
            else:
                low = partition1 + 1
