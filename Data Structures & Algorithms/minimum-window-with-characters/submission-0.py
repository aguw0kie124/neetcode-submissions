class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount, window = dict(), dict()
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1
        
        l = 0
        have, need = 0, len(tcount)
        result, length = [0, 0], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in tcount and window[c] == tcount[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    result = [l, r]
                    length = r - l + 1

                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1 
                l += 1
        
        l, r = result
        return s[l: r+1] if length != float("infinity") else ""
            


