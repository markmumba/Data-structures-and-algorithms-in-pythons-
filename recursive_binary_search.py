def recursive_binary_search(lists, target):
    if lists ==0:
        return False
    else:
        midpoint=len(lists)//2
        if lists[midpoint] == target:
            return True
        else:
            if target >lists[midpoint]:
                return recursive_binary_search(lists[midpoint:],target)
            else:
                return recursive_binary_search(lists[:midpoint],target)
            
results=recursive_binary_search([11,12,13,14,15,16,17,18,19,20,21,22],15)
print("The target is index ", results)            
                
        
        
        