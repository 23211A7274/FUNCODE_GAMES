#rock paper scissors
import random

def display():
    print("Choose one ")
    print("ROCK")
    print("PAPER")
    print("SCISSORS")


def game(c_wins,u_wins):
    
    while True:
        computer_choice=random.choice(["rock","paper","scissors"])
        user_choice=input("Choose one: or type 'quit' to quit ").lower()
        if user_choice=='quit':
            break
        
       

        if user_choice not in ['rock' , 'paper','scissors']:
            print("Please enter the valid input")
            continue

        else:
            None

        if user_choice=='paper' and computer_choice=='paper':
            print(f"computer choice is {computer_choice}")
            print("try again")
            
        elif user_choice=='paper' and computer_choice=='rock':
            print(f"computer choice is {computer_choice}")
            print("u wins")
            u_wins+=1
        elif user_choice=='paper' and computer_choice=='scissors':
            print(f"computer choice is {computer_choice}")
            print("c wins")
            c_wins+=1
        elif user_choice=='rock' and computer_choice=='rock':
            print(f"computer choice is {computer_choice}")
            print("try again")
            
        elif user_choice=='rock' and computer_choice=='paper':
            
            print(f"computer choice is {computer_choice}")
            print("c wins")
            c_wins+=1
        elif user_choice=='rock' and computer_choice=='scissors':
            print(f"computer choice is {computer_choice}")
            print("u wins")
            u_wins+=1
        elif user_choice=='scissors' and computer_choice=='scissors':
            print(f"computer choice is {computer_choice}")
            print("try again")
           
        elif user_choice=='scissors' and computer_choice=='paper':
            print(f"computer choice is {computer_choice}")
            print("u wins")
            u_wins+=1
        elif user_choice=='scissors' and computer_choice=='rock':
            print(f"computer choice is {computer_choice}")
            print("c wins")
            c_wins+=1

        else:
            None

    print("Thank you for playing ")    
    if u_wins > c_wins:
        print(f"The user have won with {u_wins} points")
    else:
        print(f"The computer won with {c_wins} points")

        
if __name__=="__main__":
    display()
    c_wins=0
    u_wins=0
    game(c_wins,u_wins)