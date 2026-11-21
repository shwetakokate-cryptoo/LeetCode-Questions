
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        stacks = [[] for _ in range(26)]

        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                stacks[c].append(node)
                stack.append((node, par, 1))

                for child in reversed(tree[node]):
                    stack.append((child, node, 0))

            else:
                if len(stacks[c]) > 1:
                    new_parent = stacks[c][-2]
                else:
                    new_parent = par

                if new_parent != -1:
                    ans[new_parent] += ans[node]

                stacks[c].pop()

        return ans
