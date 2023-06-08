def sublist(l, start, end):
    result = []
    i = start
    while i <= end:
        result.append(l[i])
        i += 2
    return result

l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
print(sublist(l, 2, 9))
