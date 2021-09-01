# Assignment

## Function Implement

### Problem 1

```
Problem: Given a string s, determine if it is a palindrome, considering only alphanumeric characters and
ignoring cases.

Solution: Using stack data structure to store the character of string, and pop out stack element with the original string
```

```python
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
```

### Problem 2

```
Problem:You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid. For example, strs =
["abc", "bce", "cae"] can be arranged as:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-
indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a')
is not, so you would delete column 1.
Return the number of columns that you will delete.

Solution: compare strings of each cols with sorted strings of cols, check if both the same
```

```python
def minDeletionSize(strs):
    res = 0
    for i in range(len(strs[0])):
        cols = [string[i] for string in strs]
        if cols != sorted(cols):
            res += 1
    return res
```

`
## Run unit test
```bash
python -m venv venv
source venv/bin/activate
pip install -r tests/requirements.txt

cd tests
pytest
```
