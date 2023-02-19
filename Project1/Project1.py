import random

def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True 
    if comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    if comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False       
            
    
print("Comp turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("the game is tie")
elif a:
    print("you win")
else : print ("you loose")
