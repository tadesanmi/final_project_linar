# A program to create a game called rock, paper, scissors
import random
choices = ("Rock", "Paper", "Scissors")
player = False
cpu_score = 0
player_score = 0
while True:
    computer = random.choice(choices)
    player = input("Rock,paper or Scissors?").capitalize()

#conditions of rock,paper and scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers" , player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes" , computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut" , player)
            cpu_score+=1
        else:
            print("You win!",player, "covers" , computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes" , player)
            cpu_score+=1
        else:
            print("You win!", player, "cuts" , computer)
            player_score+=1
    elif player == "End":
        print("Final scores:")
        print(f"CPU:{cpu_score}")
        print(f"PLAYER:{player_score}")
        break