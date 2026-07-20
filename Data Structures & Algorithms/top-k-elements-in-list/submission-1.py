class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        return sorted(freq, key=freq.get, reverse=True)[:k]
        

        