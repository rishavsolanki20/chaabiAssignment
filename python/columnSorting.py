def sortDicts(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

print(sortDicts(dicts, "fruit"))
print(sortDicts(dicts, "color"))
