from typing import List

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        nexorviant = nums
        n = len(nums)
        count = 0
        
        for i in range(n):
            current_sum = 0
            # To optimize check, we can just iterate.
            # Since constraints are N=500, O(N^3) is 1.25e8, might be slow (limit usually 10^8).
            # O(N^2) is preferred.
            for j in range(i, n):
                current_sum += nums[j]
                # Check if current_sum exists in nums[i...j]
                # We can iterate through the slice? That makes it O(N^3).
                # To do O(N^2), we need O(1) check.
                # Since 'nums[j]' is just added, we could maintain a set?
                # But space? Set creation is costly inside loop?
                # Actually constraints say N<=500.
                # If we just look at the slice, worst case 500*250*...
                # slice check: `val in arr`.
                # Python `in` is O(k).
                # Total operations: Sum(k for k=1 to N) over N iterations -> N^3 / 6.
                # 500^3 / 6 = 125,000,000 / 6 approx 20 million.
                # This should pass easily in Python for 1-2 seconds.
                if current_sum in nums[i : j+1]:
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [-1, 1, 0]
    print(f"Input: nums = {nums1}")
    print(f"Output: {sol.centeredSubarrays(nums1)}")
    print("Expected: 5\n")
    
    # Example 2
    nums2 = [2, -3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {sol.centeredSubarrays(nums2)}")
    print("Expected: 2\n")
