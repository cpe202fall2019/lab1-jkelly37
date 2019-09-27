def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None or len(int_list) == 0:
        raise ValueError
    max1 = int_list[0]
    for x in int_list:
        if x > max1:
            max1=x
    return max1


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list==None:
        raise ValueError
    else:
        if len(int_list)>0:
            return [int_list[len(int_list)-1]] + reverse_rec(int_list[:len(int_list)-1])
        else:
            return int_list

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list==None or len(int_list)==0:
        raise ValueError
    if low > target or high < target:
        return None
    if len(int_list)==2 and target!=low and target!=high:
        return None
    index= len(int_list)//2
    if target==int_list[index]:
        return index
    if target>int_list[index]:
        newList = int_list[index:]
        binReturn = bin_search(target,newList[0],newList[len(newList)-1],newList)
        if binReturn is None:
            return None
        else:
            return binReturn + index
    else:
        newList=int_list[:index+1]
        return bin_search(target,newList[0], newList[len(newList)-1],newList)









