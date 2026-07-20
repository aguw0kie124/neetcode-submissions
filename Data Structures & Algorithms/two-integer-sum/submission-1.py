class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                j = seen[complement]
                return [j, i]
            else:
                seen[nums[i]] = i