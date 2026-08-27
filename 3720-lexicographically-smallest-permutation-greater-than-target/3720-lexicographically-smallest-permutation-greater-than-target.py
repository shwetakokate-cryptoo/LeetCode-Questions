class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            idx = ord(target[i]) - ord('a')

            if count[idx] > 0:
                count[idx] -= 1
                ans.append(target[i])
                continue

            for j in range(idx + 1, 26):
                if count[j] > 0:
                    ans.append(chr(ord('a') + j))
                    count[j] -= 1

                    for k in range(26):
                        ans.extend([chr(ord('a') + k)] * count[k])

                    return ''.join(ans)

            break

        for i in range(len(ans) - 1, -1, -1):
            idx = ord(ans[i]) - ord('a')
            count[idx] += 1

            for j in range(idx + 1, 26):
                if count[j] > 0:
                    result = ans[:i]
                    result.append(chr(ord('a') + j))
                    count[j] -= 1

                    for k in range(26):
                        result.extend([chr(ord('a') + k)] * count[k])

                    return ''.join(result)

        return ""