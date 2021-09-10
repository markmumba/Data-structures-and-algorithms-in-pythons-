def binary_search(listed, target):
    first = 0
    last=len(listed)-1
    
    while first <= last:
        midpoint=(first+last)//2
        if listed[midpoint] == target:
            return midpoint
        elif target>listed[midpoint]:
            first=midpoint+1
        else:
            last=midpoint-1
            
    return None 


results = binary_search([2,3,5,7,9],7)
print("The index is ", results)