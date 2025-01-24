def BinarySearch(start,high,array,searchValue):
    middle = (start + high) // 2;
    if array[middle] == searchValue :
        return middle;
    else:
        if searchValue < array[middle]:
            return BinarySearch(start,middle-1,array,searchValue);
        elif searchValue > array[middle]:
            return BinarySearch(middle+1,high,array,searchValue);
        
array =[1,2,3,4,5,6,7,8,9,10];
index = BinarySearch(0,len(array)-1,array,5);
print("Value Found at : ", index)