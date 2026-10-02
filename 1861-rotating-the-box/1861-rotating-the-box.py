class Solution:
    def rotateTheBox(self, box):
        m = len(box)
        n = len(box[0])

        for i in range(m):
            empty = n - 1

            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][empty] = '#'
                    empty -= 1

        result = [[''] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]

        return result