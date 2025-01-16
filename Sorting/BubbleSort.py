array = [1,3,4,5,68,3,45,56,73];
print("Original array: ", array);
for i in range(len(array)-1):
    for j in range(i+1,len(array)-1):
        if array[i]>array[j]:
            temp = array[j];
            array[j]=array[i];
            array[i]=temp

print("Sorted array: ", array);