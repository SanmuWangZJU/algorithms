"""
    a quick sort implement in python
    @:author sanmu
"""


def quickSort(l):
    if len(l) <= 1:
        return l
    return quickSort([lt for lt in l[1:] if l[0] > lt] + [l[0]]) + quickSort([gt for gt in l[1:] if gt >= l[0]])

print(quickSort([3,2,56,1,2,4]))