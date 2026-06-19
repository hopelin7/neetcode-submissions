class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    stack.append(second + first)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                else:  # "/"
                    stack.append(int(second / first))

        return stack[-1]