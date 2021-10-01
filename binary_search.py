def binary_search(listed, target):
    first = 0
    last=len(listed)-1
    
    while first <= last:
        midpoint=(first+last)//2
        if listed[midpoint] == target:
            return midpoint
        else:
            if target>listed[midpoint]:
                return binary_search(listed[midpoint + 1:],target)
            else:
                return binary_search(listed[:midpoint - 1],target)
            
    return None 


results = binary_search([2,3,5,7,9],7)
print("The index is ", results)