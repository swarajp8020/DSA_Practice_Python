import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next
if __name__ == "__main__":
    a = ListNode(1, ListNode(4, ListNode(7)))
    b = ListNode(2, ListNode(5, ListNode(8)))
    c = ListNode(3, ListNode(6, ListNode(9)))
    sol = Solution()
    result = sol.mergeKLists([a, b, c])
    while result:
        print(result.val, end=" ")
        result = result.next
        