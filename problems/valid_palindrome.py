import re


pattern = '[a-zA-Z0-9]'


def isPalindrome(string):
    stack = []

    for c in string:
        if re.match(pattern, c):
            stack.append(c)

    for c in string:
        if not re.match(pattern, c):
            continue

        c_from_last = stack.pop()

        if c_from_last.lower() != c.lower():
            return False

    return True
