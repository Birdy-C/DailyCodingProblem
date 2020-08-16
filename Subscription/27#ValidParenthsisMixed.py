'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''
def isValid(str):
    stack = []
    for p in str:
        if p in {'(', '[', '{'}:
            stack.append(p)
        else:
            if p == ')' and stack[-1] != '(' \
            or p == ']' and stack[-1] != '[' \
            or p == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(isValid("{{[(])}}"))
