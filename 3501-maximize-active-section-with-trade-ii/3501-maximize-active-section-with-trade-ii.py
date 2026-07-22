from bisect import bisect_right
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if ch == '1' else 0)
        totalOnes = prefix[n]

        runsChar, runsStart, runsEnd = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runsChar.append(s[i]); runsStart.append(i); runsEnd.append(j - 1)
            i = j
        m = len(runsChar)
        runLen = [runsEnd[k] - runsStart[k] + 1 for k in range(m)]

        NEG, POS = -10**9, 10**9
        arrA, arrB, arrZ = [0]*m, [0]*m, [0]*m
        for k in range(m):
            if runsChar[k] == '1':
                arrA[k] = runLen[k]
                left = runLen[k-1] if k-1 >= 0 else 0
                right = runLen[k+1] if k+1 < m else 0
                arrB[k] = left + right
                arrZ[k] = NEG
            else:
                arrA[k] = POS
                arrB[k] = NEG
                arrZ[k] = runLen[k]

        LOG = [0] * (m + 2)
        for x in range(2, m + 2):
            LOG[x] = LOG[x // 2] + 1

        def build_sparse(arr):
            mm = len(arr)
            if mm == 0:
                return []
            table = [arr[:]]
            jlev = 1
            while (1 << jlev) <= mm:
                prev = table[-1]
                half = 1 << (jlev - 1)
                cur_len = mm - (1 << jlev) + 1
                cur = [0] * cur_len
                for idx in range(cur_len):
                    cur[idx] = prev[idx]
                table.append(cur)
                jlev += 1
            return table

        def build_sparse_op(arr, op):
            mm = len(arr)
            if mm == 0:
                return []
            table = [arr[:]]
            jlev = 1
            while (1 << jlev) <= mm:
                prev = table[-1]
                half = 1 << (jlev - 1)
                cur_len = mm - (1 << jlev) + 1
                cur = [op(prev[idx], prev[idx + half]) for idx in range(cur_len)]
                table.append(cur)
                jlev += 1
            return table

        tableA = build_sparse_op(arrA, min)
        tableB = build_sparse_op(arrB, max)
        tableZ = build_sparse_op(arrZ, max)

        def q_sparse(table, L, R, op, default):
            if L > R or not table:
                return default
            length = R - L + 1
            k = LOG[length]
            return op(table[k][L], table[k][R - (1 << k) + 1])

        def RangeMin(L, R):
            return q_sparse(tableA, L, R, min, POS)

        def RangeMaxB(L, R):
            return q_sparse(tableB, L, R, max, NEG)

        def RangeMaxZ(L, R):
            return q_sparse(tableZ, L, R, max, NEG)

        ans = []
        for l, r in queries:
            base = prefix[r + 1] - prefix[l]
            runL = bisect_right(runsStart, l) - 1
            runR = bisect_right(runsStart, r) - 1

            if runL == runR:
                ans.append(totalOnes)
                continue

            A, B = runL + 1, runR - 1

            leftZero = runsEnd[runL] - l + 1 if runsChar[runL] == '0' else 0
            rightZero = r - runsStart[runR] + 1 if runsChar[runR] == '0' else 0
            midZeroMax = RangeMaxZ(A, B)
            globalMaxZero = max(leftZero, rightZero, midZeroMax)

            if A > B:
                inner = base
            else:
                if runsChar[A] == '1':
                    first1 = A
                else:
                    first1 = A + 1 if A + 1 <= B else None
                if runsChar[B] == '1':
                    last1 = B
                else:
                    last1 = B - 1 if B - 1 >= A else None

                if first1 is None or last1 is None:
                    inner = base
                else:
                    minA_val = RangeMin(A, B)

                    def neighborL(pos):
                        if pos == A and runsChar[runL] == '0':
                            return runsEnd[runL] - l + 1
                        return runLen[pos - 1]

                    def neighborR(pos):
                        if pos == B and runsChar[runR] == '0':
                            return r - runsStart[runR] + 1
                        return runLen[pos + 1]

                    val_first1 = neighborL(first1) + neighborR(first1)
                    val_last1 = neighborL(last1) + neighborR(last1)
                    maxB_val = max(val_first1, val_last1)

                    if first1 != last1:
                        lo, hi = first1 + 1, last1 - 1
                        if lo <= hi:
                            midv = RangeMaxB(lo, hi)
                            if midv > maxB_val:
                                maxB_val = midv

                    candidate_from_zero = globalMaxZero - minA_val
                    inner = base + max(maxB_val, candidate_from_zero)

            ans.append(totalOnes - base + inner)

        return ans