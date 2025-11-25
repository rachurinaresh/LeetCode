class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 != 0:
            return []
        if n == 0:
            return []
        maxVal = max(changed)
        freq = [0] * ((maxVal * 2) + 1)
        for x in changed:
            freq[x] += 1
        if freq[0] % 2 != 0:
            return []
        org = []
        z = freq[0] // 2
        if z >0:
            org.extend([0] * z)
        for i in range(1, maxVal+1):
            if freq[i] == 0:
                continue
            if freq[i] > 1:
                c = freq[i]
                cc = freq[i*2]
                if cc < c:
                    return []
                else:
                    org.extend([i]*c)
                freq[i] = 0
                freq[2*i] -= c
            else:
                if freq[i*2] == 0:
                    return []
                org.append(i)
                freq[i] -= 1
                freq[i*2] -= 1
        return org
