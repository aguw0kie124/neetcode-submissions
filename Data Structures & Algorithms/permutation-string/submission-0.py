class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counts = dict()
        for c in s1:
            s1counts[c] = s1counts.get(c, 0) + 1
        
        l = 0
        s2counts = dict()

        for r in range(len(s2)):
            c = s2[r]
            s2counts[c] = s2counts.get(c, 0) + 1

            if (r - l + 1) > len(s1):
                s2counts[s2[l]] -= 1
                if s2counts[s2[l]] == 0:
                    del s2counts[s2[l]]
                l += 1

            if s2counts == s1counts:
                return True
        return False
            

            







        