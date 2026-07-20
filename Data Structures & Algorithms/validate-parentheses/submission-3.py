class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or pairs[c] != stack[-1]:
                    return False
                stack.pop()

        return not stack