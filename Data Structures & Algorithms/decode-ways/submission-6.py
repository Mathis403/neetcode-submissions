from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def ds(i):
            if s[i] == "0":
                return 0
            if len(s) - 1 == i:
                return 1
            
            
            res = ds(i+1)
            if ((s[i] == "1") or (s[i] == "2" and s[i+1] < "7")):
                if len(s) - (i+2) > 0:
                    res += ds(i+2)
                else:
                    res += 1
            return res
        return ds(0)