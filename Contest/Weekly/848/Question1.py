class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        count = 0
        for i, char in enumerate(s):
            seen.add(char)
            if len(seen) == (i + 1) % 3:
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "abc"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {sol.residuePrefixes(s1)}")
    print("Expected: 2\n")
    
    # Example 2
    s2 = "dd"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {sol.residuePrefixes(s2)}")
    print("Expected: 1\n")
    
    # Example 3
    s3 = "bob"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {sol.residuePrefixes(s3)}")
    print("Expected: 2\n")
