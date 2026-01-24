import random
items_list=['rock','paper','scissor']

computer_choice=random.choice(items_list)

while(True):
    user_choice=input("Enter your move: ").strip().lower()
    if user_choice=='exit':
        print("Exiting the game....")
        break

    print("User choice is :",user_choice)
    print("Computer choice is :",computer_choice)


    if user_choice==computer_choice:
        print("Tie")

    # Logic for the user to win
    elif (
        (user_choice=='rock' and computer_choice=='scissor') or
        (user_choice=='paper' and computer_choice=='rock') or
        (user_choice=='scissor' and computer_choice=='paer') 
    ):
        print("User wins")

    # Logic for the computer to win
    elif user_choice in items_list:
        print("Computer wins")


    else:
        print("Invalid choice")

    


