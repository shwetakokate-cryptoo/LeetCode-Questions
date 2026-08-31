class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        positions = []
        prev = head
        curr = head.next
        pos = 1

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                positions.append(pos)

            prev = curr
            curr = curr.next
            pos += 1

        if len(positions) < 2:
            return [-1, -1]

        minimum = min(positions[i] - positions[i - 1] for i in range(1, len(positions)))
        maximum = positions[-1] - positions[0]

        return [minimum, maximum]