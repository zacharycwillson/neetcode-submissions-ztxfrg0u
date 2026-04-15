class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                answer = num1 + num2
                stack.append(answer)
            elif t == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                answer = num1 - num2
                stack.append(answer)
            elif t == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                answer = num1 * num2
                stack.append(answer)
            elif t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                answer = int(num1 / num2)
                stack.append(answer)
            else: 
                stack.append(int(t))
        return stack.pop()
            



        
            



        