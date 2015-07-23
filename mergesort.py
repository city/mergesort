ort(splitlist):

    if(len(splitlist) <= 1):
        return splitlist

    leftL = splitlist[:len(splitlist)//2]
    rightL = splitlist[len(splitlist)//2:]

    leftL = mergesort(leftL)
    rightL = mergesort(rightL)

    return merge(leftL, rightL)

def merge(leftL, rightL):
    #check the first index of leftL against first index of rightL and put whichever is bigger into the sortedList
    sortedlist = []
    l_idx = 0
    r_idx = 0
    while(l_idx < len(leftL) and r_idx < len(rightL)):
        if(leftL[l_idx] < rightL[r_idx]):
            sortedlist.append(leftL[l_idx])
            l_idx += 1
        else:
            sortedlist.append(rightL[r_idx])
            r_idx += 1

    if (l_idx < len(leftL)):
        sortedlist.extend(leftL[l_idx:])
    if(r_idx < len(rightL)):
        sortedlist.extend(rightL[r_idx:])

    return sortedlist



list = [1, 40, 3, 27, 12, 120, 8]
print(list)
sortedList = mergesort(list)
print(sortedList)
