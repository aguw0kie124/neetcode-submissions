class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
    
        pivot = l

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            realm = (m + pivot) % len(nums)

            if nums[realm] == target:
                return realm
            elif nums[realm] < target:
                l = m + 1
            else:
                r = m - 1
            
        return -1



            


