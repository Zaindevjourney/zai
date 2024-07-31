                           # PROJECT 01 -   PIG   # 


import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2 - 4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Must be between 2 - 4 players. ")
            break
        else:
            print("Must be between 2 - 4 players. ")
    else:
        print("invalid, try again. ")


max_score = 50
players_scores =  [ 0 for _  in range(players)]


while max(players_scores) < max_score:

    for player_idx in range(players):
        print("\nplayer number",player_idx + 1, "turn has  just started! ")
        print("your total score is :",players_scores[player_idx],"\n")
        current_score = 0


    while True:
        should_roll = input("would you like to roll (y)? ")
        if should_roll.lower() != "y":
          break

        Value = roll()
        if Value== 1:
            print("you rolled a 1! turn  done!")
            current_score = 0
            break
        else:
            current_score += Value
            print("you rolled a:", Value)

        print("tour score is:", current_score)

    players_scores[player_idx] += current_score
    print("your total score is:", players_scores[player_idx])    


max_score = max(players_scores)
winnig_idx = players_scores.index(max_score)
print("player number", winnig_idx + 1, "is the winner woth a score of :", max_score)
