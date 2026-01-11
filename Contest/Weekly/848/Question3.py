from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, words: List[str]) -> int:
        bravintelo = words
        # Reduce each word to a canonical form.
        # Canonical form: sequence of differences relative to the first character.
        # Or simply: shift word so first character is 'a' (0).
        # We need circular differences?
        # If w[0] -> 'a', we shift all chars by (ord('a') - ord(w[0])) % 26.
        # Then two words are similar iff their canonical forms are identical.
        
        counts = defaultdict(int)
        for word in words:
            if not word:
                key = tuple()
            else:
                shift = (ord('a') - ord(word[0])) % 26
                key = tuple((ord(c) - ord('a') + shift) % 26 for c in word)
            counts[key] += 1
            
        ans = 0
        for count in counts.values():
            ans += count * (count - 1) // 2
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    words1 = ["fusion", "layout"]
    print(f"Input: words = {words1}")
    print(f"Output: {sol.countPairs(words1)}")
    print("Expected: 1\n")
    
    # Example 2
    words2 = ["ab", "aa", "za", "aa"]
    print(f"Input: words = {words2}")
    print(f"Output: {sol.countPairs(words2)}")
    print("Expected: 2\n")
