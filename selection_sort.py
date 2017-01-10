import random

random_list = random.sample(xrange(0,10001),100)
print "\nrandom list is: ",random_list,"\n"

from datetime import datetime
a = datetime.now()

print "length of list is ",len(random_list),"\n"

def selection_sort(arr):

    count = 0 # counts swap times
    for i in range(0,int(len(arr)/2)): #goes halfway through the array

        low = i                                                  #set current lowest index at position i
        high = i
        for j in range(i,len(arr)-i-1):                          #starts at the index of i and loops through all other indexes

            if arr[j] < arr[low]:                                #check if an index is lower than the current lowest
                low = j                                          #set low to the new lower index
            if arr[j] > arr[high]:
                high = j

        arr[i],arr[low] = arr[low],arr[i]                       #unpack tuples
        arr[len(arr)-i-1],arr[high] = arr[high],arr[len(arr)-i-1]
        count +=1

    print "sorted ",count," times\n"
    return "sorted list is: %s"%(arr)

print selection_sort(random_list)
b = datetime.now()
c = b-a
print "\nruntime is ",c
