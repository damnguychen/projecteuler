# merge 2 sorted lists

def MergeTwoSortedLists(l1, l2):
    i = 0
    j = 0
    result = []
        
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        
        else:
            result.append(l1[i])
            i += 1
                
    while i < len(l1):
        result.append(l1[i])
        i += 1
        
    while j < len(l2):
        result.append(l2[j])
        j += 1
            
    return result

print(MergeTwoSortedLists([1, 2, 4], [1, 3, 4]))
