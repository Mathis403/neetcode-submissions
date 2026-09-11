class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        m = 0
        maxf = 0
        d = {}

        for r in range(len(s)):
            if s[r] not in d.keys():
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            maxf = max(maxf, d[s[r]])
        
            while (r-l+1) - maxf > k:
                d[s[l]] -= 1
                l += 1
            res = max(m, r - l +1)
        return res

            
        