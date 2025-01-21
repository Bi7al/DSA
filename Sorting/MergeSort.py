array = [9,8,7,5,4,2,6];
def MergeSort(array):
    # Base Condition
    if len(array)<=1:
        return array;
    
    #  Splitting Array
    mid = len(array)//2;
    leftHalf = array[:mid]
    righHalf= array[mid:]
    sortedLeft=MergeSort(leftHalf);
    sortedRight=MergeSort(righHalf);
    #  Sorting 
    i=j=0;
    result = []
    while i < len(sortedLeft) and j < len(sortedRight):
        if sortedLeft[i] < sortedRight[j]:
            result.append(sortedLeft[i]);
            i=i+1;
        elif sortedLeft[i]>sortedRight[j]:
            result.append(sortedRight[j]);
            j+=1;
        elif sortedLeft[i]==sortedRight[j]:
            result.append(sortedLeft[i]);
            result.append(sortedRight[j]);
            i+=1;
            j+=1;
    result.extend(sortedLeft[i:]);
    result.extend(sortedRight[j:]);
    
    return result;

    
print("Original Array : ",array);
array=MergeSort(array)
print("Sorted Array : ", array)
