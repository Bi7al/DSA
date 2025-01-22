def CountingSort(array):
    count_array = [0]*(max(array)+1);
    for i in range(len(array)):
         count_array[array[i]]+=1;
    result =[]   
    for i in range(len(count_array)):
        for j in range(count_array[i]):
            result.append(i);
            
    return result;


array = [2,2,2,2,2,4,4,4,4,3,4,5,5,5,3,3,3,3,1,1,1,1];
print("Original Array : ",array);
result = CountingSort(array);
print("Sorted Array : ",result);