def index_power(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n] ** n
print("index_power([1,2,3,4],2) = ", index_power([1,2,3,4],2))
print("index_power([1,3,10,100],3 = ", index_power([1,3,10,100],3))
print("index_power([0,1],0) = ", index_power([0,1],0))
print("index_power([1,2],3) = ", index_power([1,2],3))
