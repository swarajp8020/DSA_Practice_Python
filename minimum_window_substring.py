from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = {}
        required = len(need)
        formed = 0

        left = 0
        ans = (float("inf"), None, None)
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed+=1
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
if __name__ == "__main__":
    sol = Solution()
    s = "ssadafa"
    t = "sad"
    print(sol.minWindow(s,t))