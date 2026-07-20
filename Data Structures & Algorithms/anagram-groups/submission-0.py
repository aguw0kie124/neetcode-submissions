class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()

        for s in strs:
            key = tuple(sorted(s))

            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
    
        return list(anagram_map.values())
            
    

        