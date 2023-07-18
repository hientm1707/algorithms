

input = [1,9,4,6,88,66,44,22,48,9]

def selection_sort(lst):
    for i in range(len(lst)): 
        min_idx = i #Mark first element as the smallest
        for j in range(i+1, len(lst)): #Find the smallest on the unsorted array
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst




        
selection_sort(input)
print(input)
        
            
