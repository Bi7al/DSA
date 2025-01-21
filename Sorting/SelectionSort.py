array=[4,55,8,3,1,34]
print("Original Array : ",array);
def SelectionSort(array):
    for i in range(len(array)-1):
        min_index= i;
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index=j
        temp = array[i];
        array[i]=array[min_index];
        array[min_index]=temp;
    
SelectionSort(array);
print("Sorted Array : ",array);