import random

# making list of game
item_list =["Rock", "Paper", "Scissor"]

#taking input from user and computer
user_choice = input("Enter your choice:(Rock, Paper, Scissor)")
comp_choice = random.choice(item_list)

# showing user and computer choices
print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

# if both choses same
if user_choice == comp_choice:
    print("Ops same choice Match Tie.....")

# when user choses rock
elif user_choice == "Rock" :
    if comp_choice == "Paper":
        print("Paper cover rock Computer Win..")
    elif comp_choice == "Scissor":
        print("Rock smash scissor User Win..")
    else :
        print("Invalid choice")

# when user choses paper
elif user_choice == "Paper" :
    if comp_choice == "Rock":
        print("Paper cover rock User Win..")
    elif comp_choice == "Scissor":
        print("Scissor cuts paper Computer Win..")
    else :
        print("Invalid choice")

# when user choses scissor
elif user_choice == "Scissor" :
    if comp_choice == "Paper":
        print("Scissor cuts paper User Win..")
    elif comp_choice == "Rock":
        print("Rock smash scissor Computer Win..")
    else :
        print("Invalid choice")
else :
        print("Invalid choice")