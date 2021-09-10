def linear_search (lists, target):
    
    for i in range(0, len(lists)):
        if lists[i]==target:
            return i
    return None

results= linear_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14],10)
print (results)
            