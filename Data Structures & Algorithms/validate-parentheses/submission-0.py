class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            else:
                if not stack or stack.pop() != c:
                    return False

        return not stack