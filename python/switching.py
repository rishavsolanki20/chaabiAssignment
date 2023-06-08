def switchDict(d):
    result = {}
    for key, value in d.items():
        result[value] = key
    return result

d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

print(switchDict(d))
