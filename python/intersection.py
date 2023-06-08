def compare_lists(a, b):
    aSet = set(a)
    bSet = set(b)
    intersection = list(aSet.intersection(bSet))
    symmetricDifference = list((aSet | bSet) - (aSet & bSet))
    return intersection, symmetricDifference

mainStream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

print(compare_lists(mainStream, must_watch))