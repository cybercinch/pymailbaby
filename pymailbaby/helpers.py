
def MergeDict(dict1, dict2):
    dict2.update(dict1)
    return dict2

def RemoveFromString(items, string):
    for item in items:
        string = string.replace(item, '')
    return string

def EnsurePositiveInteger(number):
    return float(number) if float(number) > 0 else (float(number) * -1)