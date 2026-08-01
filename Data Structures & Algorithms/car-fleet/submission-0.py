class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        stack = []

        for p, s in sorted(pairs, reverse=True):
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return(len(stack))