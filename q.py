# import os

# print(os.getcwd())


class List:

    def __init__(self, list):
        self.list = list

    def listed(self):
        return self.list

    def get_count(self):
        count = 0
        for i in range(len(self.list)):
            count +=1
        return count

    def add_all_values(self):
        count=0
        for i in self.list:
            count += i
        return count

    def get_largest_number(self):

        return max(self.list)
        
    def remove_number(self, number):

        return self.list.remove(number)

    def split(self):
    
        midpoint=len(self.list)//2
        left= self.list [:midpoint]
        right= self.list [midpoint:]

        return left,right

    def merge(self ,left,right):

        l=[]
        i=0
        j=0
        while i<len(left) and j< len(right):
            if left[i]< right[j]:
                l.append(left[i])
                i +=1
            else:
                l.append(right[j])
                j+=1
            while i < len(left):
                l.append(left[i])
                i+=1   
            while j < len(right):
                l.append(right[j])
                j+=1

            return 1


    def merge_sort(self):
    
        if len(self.list) <= 1:
            return self.list

        leftside,rightside = List.split(self.list)
        left =List.merge_sort(leftside)
        right = List.merge_sort(rightside)

        return List.merge(left,right)


    def find_number (self, target):
        new_list=sorted(self.list)
        print(self.list)
        first = 0
        last= len(new_list)-1
        while first <= last:
            midpoint=(first+last)//2
            if new_list[midpoint] == target:
                return f"the index is {midpoint}"
            elif new_list[midpoint] < target:
                first=midpoint +1
            else:
                last= midpoint -1
        return None
 
    def add_two_lists(self, other):
        result=[]
        for i in range(len(self.list)):
            result.append(self.list[i]+ other.list[i])
        return result



