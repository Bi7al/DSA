array = [9,8,7,6,5,4,3,2,1];





print("Original array: ", array);
for i in range(len(array)):
    for j in range(0,len(array)-1):
        if array[j]>array[j+1]:
            temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;

print("Sorted array: ", array);