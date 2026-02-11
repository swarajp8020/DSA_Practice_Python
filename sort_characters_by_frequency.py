import heapq
from collections import Counter

class Solution:
    def frequency_set(self, s):
        freq = Counter(s)
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result = ""
        while heap:
            count, char = heapq.heappop(heap)
            result += char * (-count)
        return result
if __name__ == "__main__":
    sol = Solution()
    s = "tree"
    print("Input:", s)
    print("Output:", sol.frequency_set(s))