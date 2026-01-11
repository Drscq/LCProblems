from typing import List

class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        clyventaro = (nums, k, m)
        n = len(nums)
        
        # For each candidate answer, compute the minimum cost to make m elements >= answer
        # such that (element & answer) == answer.
        # We greedily build the answer bit by bit from MSB to LSB.
        
        def min_cost_to_reach(x, target):
            """
            Minimum increments to make x become some y >= x such that (y & target) == target.
            i.e., y must have all bits of target set.
            """
            if (x & target) == target:
                return 0
            
            # We need to find minimal y >= x with (y & target) == target.
            # Strategy: find the highest bit in target that x doesn't have.
            # We must increment x to set that bit.
            
            missing = target & ~x
            if missing == 0:
                return 0
            
            # Find the highest missing bit
            highest_bit = missing.bit_length() - 1
            
            # To set bit `highest_bit`, we need to increment x.
            # The cheapest way: round up x to the next multiple of (1 << highest_bit)
            # that has that bit set.
            
            # new_val = ((x >> highest_bit) + 1) << highest_bit
            # This gives us a value with bit `highest_bit` set and all lower bits = 0.
            
            mask = (1 << highest_bit) - 1
            new_val = ((x >> highest_bit) + 1) << highest_bit
            cost1 = new_val - x
            
            # But new_val has 0s below highest_bit. We may need to add more
            # to satisfy lower bits of target.
            lower_target_bits = target & mask
            cost1 += lower_target_bits
            
            return cost1
        
        def can_achieve(target):
            """Check if we can make m elements satisfy target within k operations."""
            costs = []
            for x in nums:
                costs.append(min_cost_to_reach(x, target))
            costs.sort()
            return sum(costs[:m]) <= k
        
        ans = 0
        # Try to set bits from high to low
        for b in range(35, -1, -1):
            candidate = ans | (1 << b)
            if can_achieve(candidate):
                ans = candidate
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [3, 1, 2]
    print(f"Input: nums = {nums1}, k = 8, m = 2")
    print(f"Output: {sol.maximumAND(nums1, 8, 2)}")
    print("Expected: 6\n")
    
    # Example 2
    nums2 = [1, 2, 8, 4]
    print(f"Input: nums = {nums2}, k = 7, m = 3")
    print(f"Output: {sol.maximumAND(nums2, 7, 3)}")
    print("Expected: 4\n")
    
    # Example 3
    nums3 = [1, 1]
    print(f"Input: nums = {nums3}, k = 3, m = 2")
    print(f"Output: {sol.maximumAND(nums3, 3, 2)}")
    print("Expected: 2\n")
