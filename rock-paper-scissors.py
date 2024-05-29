import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Get user choice and validate input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Ensure the user choice is within the valid range
while user_choice > 2 or user_choice < 0:
    print("Please choose a valid option: 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Print the user's choice
print(f"You chose:\n{game_images[user_choice]}")

# Computer makes its choice
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_images[computer_choice]}")

# Determine the outcome
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose")
else:
    print("It's a draw")
