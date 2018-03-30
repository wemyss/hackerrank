class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        curr_len = 0
        seen = {}

        for index, c in enumerate(s):
            if c in seen and (index - seen[c] <= curr_len):
                max_len = max(curr_len, max_len)
                curr_len = index - seen[c]
            else:
                curr_len += 1

            seen[c] = index

        return max(curr_len, max_len)




s = Solution()
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring("aa"))
print(s.lengthOfLongestSubstring("aaaa"))
print(s.lengthOfLongestSubstring("abc"))
print(s.lengthOfLongestSubstring("qweq"))
print(s.lengthOfLongestSubstring("qwertyy"))
