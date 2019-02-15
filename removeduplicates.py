#Remove Duplicates

names = ["Alex","John","Mary","Steve","John", "Steve"]

def find_dupes(list):
    nondupes = []
    for name in list:
        if name not in nondupes:
            nondupes.append(name)
    return nondupes

print(find_dupes(names))
