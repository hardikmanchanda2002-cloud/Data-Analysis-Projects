import random

def game_win(user,computer):
    if user==computer:
        return None
    #water vs snake
    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
        return False
    #snake vs gun
    if user=="s" and computer=="g":
        return False
    if user=="g" and computer=="s":
        return True
    #gun vs water       
    if user=="g" and computer=="w":
        return False    
    if user=="w" and computer=="g":
        return True 

rand_no=random.randint(1, 3)
print("Computer's Turn: Snake(s), Water(w), or Gun(g)?")
if rand_no==1:
    computer="s"
elif rand_no==2:
    computer="w"
else:
    computer="g"
user=input("Your Turn: Snake(s), Water(w), or Gun(g)?").lower()
result=game_win(user,computer)#returns true for win, flase for loose,none for draw
print(f"Computer chose {computer}")
print(f"You chose {user}")

if(result is None):
    print("its a draw")
elif(result):
    print("You win!")
else:
    print("You lose!")

    
