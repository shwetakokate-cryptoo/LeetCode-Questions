
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if i < 0 or i >= n or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)

            stack.append(i + arr[i])
            stack.append(i - arr[i])

        return False
