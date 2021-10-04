#!/usr/bin/env python3
def stack():
       
   stack=[]
   print("welcome to stack \n")
   while True:
      print ("this are the letters to use an-add number,rn-remove number,ds-display the stack ex-exit ")
      user_input = input()

      if user_input == 'an':    
         print ("Enter the number you want to add") 
         number = input ()
         stack.append(int(number))
         
         
      elif user_input == 'rn':
         print(f"the last element was removed {stack.pop()}")

      elif user_input == 'ds':
         present=[]
         print( stack)
         

      elif user_input == 'ex' :     
         print ("see you later")
         break
         
      else:
         print ("invalid response")



if __name__=='__main__':
   stack()