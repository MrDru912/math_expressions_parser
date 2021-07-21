def expression_is_correct():
    pass


def expression_is_balanced(tokens):
    stack = []
    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def get_priority(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    else:
        return 0


def breakOnNumbersAndOperators(problem):
    tokens = []
    chars = list(problem)
    num = ""
    beforeWasBigNum = False
    for i in range(len(chars)):
        if i != len(chars) - 1:
            if chars[i].isnumeric():
                num += chars[i]
                beforeWasBigNum = True
            else:
                if beforeWasBigNum:
                    tokens.append(num)
                    num = ""
                    beforeWasBigNum = False
                tokens.append(chars[i])
        else:
            if beforeWasBigNum:
                num += chars[i]
                tokens.append(num)
                num = ""
                beforeWasBigNum = False
            else:
                tokens.append(chars[i])
    return tokens


def indixToPostfix(tokens):
    postfix = []
    operators = []
    for token in tokens:
        if token.isnumeric():
            postfix.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while not len(operators) == 0 and not operators[-1] == "(":
                postfix.append(operators[-1])
                operators.pop()
            operators.pop()
        elif len(operators) == 0:
            operators.append(token)
        elif get_priority(operators[-1]) < get_priority(token):
            operators.append(token)
        elif get_priority(operators[-1]) >= get_priority(tokens):
            while (not len(operators) == 0 and get_priority(operators[-1]) >= get_priority(tokens)):
                postfix.append(operators[-1])
                operators.pop()
            operators.append(token)

    while not len(operators) == 0:
        postfix.append(operators[-1])
        operators.pop()
    return postfix


def countPostfixExpression(postfixTokens):
    stack = []
    for token in postfixTokens:
        if str.isnumeric(token):
            stack.append(token)
        else:
            n2 = float(stack[-1])
            stack.pop()
            n1 = float(stack[-1])
            stack.pop()
            if token == "+":
                stack.append(n1 + n2)
            elif token == "-":
                stack.append(n1 - n2)
            elif token == "*":
                stack.append(n1 * n2)
            elif token == "/":
                stack.append(n1 / n2)
    return float(stack[-1])


if __name__ == '__main__':
    problem = "(1+10)*2"
    nums_and_operands = breakOnNumbersAndOperators(problem)
    print(nums_and_operands)
    postfix = indixToPostfix(nums_and_operands)
    print(postfix)
    print(countPostfixExpression(postfix))

    problem = "()(3*4+(2/3))"
    print(problem)
    print(expression_is_balanced(breakOnNumbersAndOperators(problem)))
    print("whats up github")
