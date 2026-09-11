class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            e = 0

            while (i-e >= 0) and (i+e < len(s)) and (s[i+e] == s[i-e]):
                res += 1
                e += 1
            
            l, r = i, i+1

            while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                l -= 1
                r += 1
                res += 1
        return res

