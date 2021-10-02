def main():

 import random
  
 print('''INSTRUCTIONS:-
  1) To choose rock, type 'r'.
  2) To choose paper, type 'p'.
  3) To choose scissor, type 's'.''')
  
 def gameWin(comp, you):
   if comp==you:
     return None
   elif comp=='r':
     if you=='p':
          return True
     elif you=='s':
          return False
     
   elif comp=='p':
     if you=='r':
          return False
     elif you=='s':
          return True
        
   elif comp=='s':
     if you=='r':
          return True
     elif you=='p':
          return False
        
  # print("Computer's turn:Rock(r) Paper(p) or Scissor(s)? ")

 randNo = random.randint(1, 3)
  
 if randNo == 1:
  comp = 'r'
 if randNo == 2:
  comp = 'p'
 if randNo == 3:
  comp = 's'
    
 you = input("Your Turn: ")
 com = print("Computer's Turn: ", comp)
 if you == "":
   print("Please enter a letter(r, p or s)!")
  
 a = gameWin(comp, you)
  
 if a == None:
   print("👍 The game is a Tie!👍")
    
 elif a:
   print("🤟 You Win!🤟")
   print() 
 else:
   print("😰 You Lose!😰")
   
 repeat = ("")
 
 if repeat == "" :
   main()
   
 else:
   exit()