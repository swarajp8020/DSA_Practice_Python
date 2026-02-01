class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')]+=1
        for i in range(len(s2)):
            freq2[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if freq1 == freq2:
                return True
        return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))