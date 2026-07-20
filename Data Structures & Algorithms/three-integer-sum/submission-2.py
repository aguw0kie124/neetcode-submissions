class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            l = i+1
            r = len(nums) - 1
            while l<r:
                s = nums[i] + nums[l] + nums[r]

                if s==0:
                    result.add((nums[i],nums[l],nums[r]))
                    #keep chekcing l and r combos in case another 0 match for i
                    l += 1
                    r -= 1
                elif s<0:
                    l += 1
                else:
                    r -= 1
    
        res = []
        for r in result:
            res.append(list(r))
        
        return res
