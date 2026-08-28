class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        mid = ""

        for i in range(26):
            if count[i] % 2:
                if mid:
                    return ""
                mid = chr(i + 97)

        half = n // 2
        half_count = [x // 2 for x in count]
        path = []
        result = ""

        def build(pos, tight):
            nonlocal result

            if result:
                return

            if pos == half:
                left = ''.join(path)
                candidate = left + mid + left[::-1]

                if candidate > target:
                    result = candidate

                return

            t = ord(target[pos]) - 97 if tight else 0

            for c in range(t, 26):
                if half_count[c] == 0:
                    continue

                half_count[c] -= 1
                path.append(chr(c + 97))

                build(pos + 1, tight and c == t)

                path.pop()
                half_count[c] += 1

                if result:
                    return

        build(0, True)

        return result