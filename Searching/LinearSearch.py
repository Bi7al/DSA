def LinearSearch(value,array):
    length = len(array);
    for i in range(length):
        if array[i] == value:
            print("Value Found At index ",i)
            return i;
    print("Value not Found")
    return -1;
array = [1,2,4,64,4,7,567,2,56,32];
index = LinearSearch(4,array)
