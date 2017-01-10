import random

random_list = random.sample(xrange(0,10001),100)

print "\nrandom list is: ",random_list,"\n"

def selection_sort(arr):
    for i in range(0,len(arr)):
        low = i                                                     #goes through every index
        for j in range(i,len(arr)):                              #starts at the index of i and loops through all other indexes
            if arr[j] < arr[low]:                                #check if an index is lower than the current lowest
                low = j                                          #set low to the new lower index
        arr[i],arr[low] = arr[low],arr[i]                       #unpack tuples
    return "sorted list is: %s"%(arr)

print selection_sort(random_list)
