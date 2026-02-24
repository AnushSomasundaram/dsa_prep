array = [1,2,3,4,5,6,7,8,9,10]

my_array = [64, 34, 25, 12, 22, 11, 90, 5]


# Bubble Sort Implementation

def bubblesort(my_array):
    
    
    
    
    for i in range(len(my_array)):
        
        pointer_1 = 0
        pointer_2 = pointer_1+1 
        
        while pointer_2< len(my_array):
            
            if my_array[pointer_1]>my_array[pointer_2]:
                temp = my_array[pointer_2]
                my_array[pointer_2] = my_array[pointer_1]
                my_array[pointer_1] = temp
                print(my_array)
            pointer_1 = pointer_1 +1
            pointer_2 = pointer_1 + 1
                
    return(my_array)

    # n = len(my_array)
    # for i in range(n-1):
    #     for j in range(n-i-1):
    #         if my_array[j] > my_array[j+1]:
    #             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]


# print(bubblesort(my_array))

# selection sort


def selection_sort(my_array):
    
    n = len(my_array)
    for i in range(n-1):
        
        min_index = i
        for j in range (i+1,n):
            
            if my_array[j]<my_array[min_index]:
                min_index = j
                
            min_value = my_array.pop(min_index)
            my_array.insert(i,min_value)
    
    print("Sorted array:", my_array)
        
        
        
#selection_sort(my_array)
          
                
# insertion sort

def insertion_sort(my_array):
    
    n = len(my_array)
     
    for i in range (1,n) :
         
        insert_index = i
         
        current_value = my_array.pop(i)
        for j in range (i-1 , -1,-1):
             if my_array[j] > current_value:
                 
                 insert_index = j
        
        my_array.insert(insert_index,current_value)
    
    print("sorted array", my_array)
        
     
#  Quick Sort

def quick_sort(my_array,low,high):
    
    
    def partition(my_array,low,high):
        pivot = my_array[high]
        
        i = low -1
        
        for j in range(low,high):
            
            if my_array[j] <= pivot:
                
                i += 1
                my_array[i], my_array[j] = my_array[j], my_array[i]
        
        
        my_array[i+1] , my_array[high] = my_array[high] , my_array[i+1]
        return i+1
    
    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = partition(array, low, high)
            quicksort(array, low, pivot_index-1)
            quicksort(array, pivot_index+1, high)

    my_array = [64, 34, 25, 12, 22, 11, 90, 5]
    quicksort(my_array)
    print("Sorted array:", my_array)
        
    
    
    

# Counting Sort

def counting_sort(my_array):
    pass

# Radix Sort

def radix_sort(my_array):
    
    pass

# Merge Sort

def merge_sort(my_array):
    
    pass

# Linear Search

def linear_search(my_array,target_val):
    
    def logic(my_array,target_val):
    
        for i in range(len(my_array)):
            
            if my_array[i] == target_val:
                return i
        
        else:
            return -1
    
    
    result = logic(my_array,target_val)
    
    if result != -1:
        print("Value",target_val,"found at index",result)
    else:
        print("Value",target_val,"not found")
        
# linear_search(my_array,36)
        
        
# Binary search

def binary_search(my_array,target_val):
    
    
    
    def logic(my_array,target_val):
    
        left = 0
        right = len(my_array) -1
        
        while left <= right:
            
            mid = (left + right)//2
            
            if my_array[mid] == target_val:
                return mid

            if my_array[mid] < target_val:
                left = mid +1
            
            else:
                right = mid -1
            
        
        return -1

    result = logic(my_array, target_val)

    if result != -1:
        print("Value", target_val,"found at index", result)
    else:
        print("Target not found in array.")
        

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

binary_search(myArray, myTarget)