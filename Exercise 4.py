def chunking_by(list, size):
    return [list[i:i+size] for i in range(0, len(list), size)]

print("chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == ", chunking_by([5,4,7,3,4,5,4],3))
print("chunking_by([3, 4, 5], 1) == ", chunking_by([3, 4, 5], 1))
