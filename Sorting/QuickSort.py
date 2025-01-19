# If curr val <= pivot value
#::: if currval == swapvalue  : pass
#::: if currVal > Swap : Swap values
# swap swap values with  pivot value
def quicksort(array, start,high):
    if(len(array)==1 or start >= high):
        return array;
    else:
        swap_Index = start-1;
        pivot_value =  array[high];
        for current_Index in range(start,high+1):
            if array[current_Index]<=pivot_value:
                swap_Index+=1;
                if current_Index > swap_Index :
                    swap = array[swap_Index];
                    array[swap_Index] = array[current_Index];
                    array[current_Index] = swap; 
                
            elif array[current_Index]> pivot_value:
                pass;
            
        quicksort(array,start,swap_Index-1);
        quicksort(array,swap_Index+1,high);
        
array = [9,8,7,6,5,4,3,2,1,0];
quicksort(array,0,len(array)-1);
print(array)
                
