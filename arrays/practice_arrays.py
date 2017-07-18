#I tried to implement assignment from https://github.com/atultherajput/coding-interview-university/tree/progress#arrays

def size(x):                                                #Get size/length of array
    return len(x)

def is_empty(x):                                        #Get True if array is empty
    if x == []:
        return True
    else:
        return False

def at(x, index):                                          #Get value of that index
    try:
        return x[index]
    except IndexError:
        return "Index Out of Range"

def push(x, item):                                             #Add iteam at end alternative of append
    x += [item]
    return x

def insert(x, index, item):                          #insert element ar given index
    x[index:index] = [item]
    return x

def prepend(x, item):                                   #insert element at beginning
    x[0:0] = [item]
    return x

def pop(x):                                                     #delete last elemnt of list
    r = x[-1]
    del x[-1]
    return r

def delete(x, index):                                     #delete element at index
    r = x[index]
    del x[index]
    return r

def remove(x, item):                                     #delete given item even in multiple place
    c=0
    for i in range(len(x)):
        if i>=len(x):
            break
        if x[i]== item:
            del x[i]
            c+=1
    r = "Removed "+str(c)+" items"
    return r

def find(x, item):                                              #find the first occurence of given element and return its index
    for i in range(len(x)):
       if x[i]== item:
            return i
    else:
        return -1


arr= [2**x for x in range(8)]               #Implemented a mutable array with automatic resizing [1, 2, 4, 8, 16, 32, 64, 128]

print(arr)                                               #[1, 2, 4, 8, 16, 32, 64, 128]

print(size(arr))                                      #8

print(is_empty(arr))                              #False

print(at(arr, 4))                                       #16

print(push(arr, 256))                               #[1, 2, 4, 8, 16, 32, 64, 128, 256]

print(insert(arr, 4, 10))                            #[1, 2, 4, 8, 10, 16, 32, 64, 128, 256]

print(prepend(arr, 512))                           #[512, 1, 2, 4, 8, 10, 16, 32, 64, 128, 256]

print(pop(arr))                                             #256

print(delete(arr, 5))                                      #10

print(remove(arr, 512))                                #Removed 1 items

print(find(arr, 64))                                         #6

print(arr)                                                         #[1, 2, 4, 8, 16, 32, 64, 128]
