array = [9,8,7,6,5,4,3,2,1];
for i in range(len(array)):
    current_val = array[i];
    for j in range(i-1,-1,-1):
        if current_val<array[j]:
            array[j+1] = array[j];
            array[j] = current_val;
        else:
            break;

print("Sorted Array : ",array);