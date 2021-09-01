def minDeletionSize(strs):
    res = 0
    for i in range(len(strs[0])):
        cols = [string[i] for string in strs]
        if cols != sorted(cols):
            res += 1
    return res
