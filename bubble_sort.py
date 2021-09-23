
def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0,len(array)-i-1):
            
            if array[j]>array[j+1]:
                var=array[j]
                array[j]=array[j+1]
                array[j+1]=var
                
                swapped=True
                
        if not swapped:
            break
            
                
    return array
                
       
    
    
data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)
                
                
# def max_multiple(divisor, bound):
#     lim =[]
#     for i in range (divisor, bound):
#         if (i % divisor==0)and i > 0 and i <= bound :
#             lim.append(i)

#     # x= sorted(lim,reverse =True)
#     return (lim[-1])

# test=max_multiple(7,100)
# print(test)

  
  

