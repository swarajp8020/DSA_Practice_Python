class Solution:
    def characterReplacement(self, s,k):
        freq = [0]*26
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')
            freq[idx] += 1
            maxFreq = max(maxFreq, freq[idx])
            while (right - left + 1) - maxFreq > k:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("sada", 2))