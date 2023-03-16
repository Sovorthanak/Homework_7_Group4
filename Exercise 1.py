def replace_last(list):
    if len(list) <= 1:
        return list
    else:
        list.insert(0, list.pop(-1))
        return list

print("replace_last([2, 3, 4, 1]) ==", replace_last([2, 3, 4, 1]))
print("replace_last([1, 2, 3, 4]) ==", replace_last([1, 2, 3, 4]))
print("replace_last([1]) == ", replace_last([1]))
print("replace_last([]) ==", replace_last([]))