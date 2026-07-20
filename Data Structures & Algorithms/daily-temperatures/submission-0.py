class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        #will store decreasing order
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            #compares current temp to lowest value in stack
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
            
            stack.append(i)
        
        return result
