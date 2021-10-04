
# class Polynimial:

#     def __init__(self, *coeffs):
#         self.coeffs = coeffs

#     def __repr__(self):
#         return f'Polynomial(*){self.coeffs}'
        
#     def __add__(self,other):
#         return Polynimial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))
    
#     def __len__(self):
#         return len(self.coeffs)


# p1=Polynimial(1,2,3)
# p2=Polynimial(5,3,4)
import  itertools
import random
# x=list(itertools.starmap(lambda a,b,c:(a**b)+c,[(0,5,10),(5,5,12),(9,5,30),(3,5,12)]))
# print (x)

# counter = itertools.count(start=30,step=50)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# def convert_to_int(x):
#     return int(x)

# x=["2","4","9","1","7","5"]

# int_str=list(map(convert_to_int,x))
# print(int_str)



# x=[4,4,4,4]
# y=[4,4,4,4]

# x=list(map(lambda a: a+a,x))
# print(x)

# import  re


# def remove_punctuation(word):
#     return re.sub(r'[!?.:;,"()-]',"",word)

# word="!the,lion,wa;roe:roepk""fj!-gol[kks]"
# text=word.split(',')

# result=list(map(remove_punctuation,text))
# print("".join(result))


# passcode=[0,1,2,3]

# result=itertools.product(passcode,repeat=5)

# for i in result:
#     print (i)

# add_number=[4,3,5,7,8,2,1]

# added=itertools.accumulate(add_number,max)
# print(list(added))

# def first_non_repeating_letter(string):
#     count=0
#     dict={}
#     if not string: 
#         return ""
#     string_lowercase=string.lower()
#     new_string=list(string_lowercase)
#     for letter in new_string:
#         letter.isupper()==letter.islower()
#         dict[letter]=new_string.count(letter)
#         for key,value  in dict.items():
#             if value == 1 :
#                 return key
                
#         if not key:
#             return ""
       
#     for x in range(0, len(string_lowercase)):
#         if string_lowercase[x] == key:
#             index = x
#             break
#     non_repeating_char_correct_case = string[x] 
#     return non_repeating_char_correct_case

# test=first_non_repeating_letter('sTreSS')
# print(test)

