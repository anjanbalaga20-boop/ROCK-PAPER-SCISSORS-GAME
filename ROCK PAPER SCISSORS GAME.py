
import random
def choose():
    print("choose 1 for Rock     🪨")
    print("choose 2 for Paper    📄")
    print("choose 3 for Scissors ✂")
    print("\n------------------")
    choice=int(input("enter your choice:"))
    if choice==1:
        return "🪨"
    elif choice==2:
        return "📄"
    elif choice==3:
        return "✂"
    else:
        print("enter only the given number")
def retry():
    retrying=input("Do you want to play Again:")
    print("-------------------------------------")
    if retrying =="yes" or retrying== "YES":
        game()
        
    else:
        print("I Think You Dont Know How To Play! That's why you are telling no ?")
 
def game():
    
    computer=random.randint(1,3)
    player=choose()
    computer=random.randint(1,3)
    if computer==1:
        computer="🪨"
    elif computer ==2:
        computer= "📄"
    else :
        computer= "✂"
    print("\n--------------------")
    print("player:",player)
    print("computer:",computer)
    
    if player==computer:
        print("draw match!")
        
        print("\n------------------")
        retry()
    elif player=="Rock" and computer=="Paper":
        print("you win!")
        print("\n------------------")
        retry()
    elif player== "Paper " and computer=="Scissors":
        print("you win!")
        print("\n------------------")
        retry()
    elif player=="Scissor" and computer=="Rock":
        print("you win!")
        print("\n------------------")
        retry()
    
    else:
        
        print("Computer Win!")
        print("\n------------------")
        retry()
game()

