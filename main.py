#we are going to design a snake , water , gun game using python programming language.


import random

def game_win(comp,you):
    #if two values are equal its a tie.
    if comp == you:
        return None 
    #check all possibilities when computer choosed snake.
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True 
    
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
        
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True 
        
print('Comp Turn: Snake(s) , Water(w), Gun(g)')


randno = random.randint(1,3)

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input('Enter your choice: Snake(s) , Water(w), Gun(g)')

a = game_win(comp,you)

print(f"Comp choosed: {comp}")
print(f"You choosed: {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You Win")
else :
    print("Hey, you loose!")








