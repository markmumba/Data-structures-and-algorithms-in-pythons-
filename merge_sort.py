def merge_sort(lists):
    
    if len(lists) <= 1:
        return lists
    
    left_half,right_half =split(lists)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    
    return merge(left, right)

def split(listed):
    
    midpoint=len(listed)//2
    left=listed[:midpoint]
    right=listed[midpoint:]
    print(left,right)
    
    return left, right
        
def merge(left, right):
    l=[]
    i=0
    j=0
    
    while i < len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    
    
    while i < len(left):
        l.append(left[i])
        i+=1
        
    while j < len(right):
        l.append(right[j])
        j+=1
            
    return l         
jpg=[99,45,33,4,2,54,67,17,32,22,88,91,5,1]
l=merge_sort(jpg)
# x=verify_sorted(l)
print(l)
# print(x)


