class Solution(object):
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        longest_so_far = ""
        current_longest = ""
        dup = {}
        for ind, let in enumerate(s):
            if let in dup and let in current_longest:
               current_longest = s[dup[let]+1:ind+1] 
            else:
                current_longest += let
            dup[let] = ind
            if len(current_longest) > len(longest_so_far):
                longest_so_far = current_longest
        return len(longest_so_far)


s = "tmmzuxt"
s = 'bbtablud'
sol = Solution()
print(sol.lengthOfLongestSubstring(s))