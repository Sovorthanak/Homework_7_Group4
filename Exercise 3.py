def remove_all_after(list, border):
    if not list:
        return list
    try:
        idx = list.index(border)
    except ValueError:
        return list
    else:
        return list[:idx+1]
print("remove_all_after([1, 2, 3, 4, 5], 3) = ", remove_all_after([1,2,3,4,5],3))
print("remove_all_after([1, 1, 2, 2, 3, 3], 2) = ", remove_all_after([1,1,2,2,3,3],2))