# If curr val <= pivot value
#::: if currval == swapvalue  : pass
#::: if currVal > Swap : Swap values
# swap swap values with  pivot value
def quicksort(array, start=0,high="none"):
    if(start == high):
        return array;
    else:
        length = len(array);
        swap_Index = start;
        pivot_value = array[high];
        for current_Index in range(start,high+1):
            if array[current_Index]<=pivot_value:
                if current_Index > swap_Index :
                    swap = array[swap_Index];
                    array[swap_Index] = array[current_Index];
                    array[current_Index] = swap; 
                    
                       
                
                ++swap_Index;
            if array[current_Index]> pivot_value:
                pass;
                
