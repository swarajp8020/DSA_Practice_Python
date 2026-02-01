class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            ans = max(ans, right - left + 1)
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("asvavsaffg"))