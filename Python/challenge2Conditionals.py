# Challenge 2 - Conditionals - Rock, Paper, Scissors

# We'll use what we've so far to create the Rock, Paper, Scissors game. Here's how:

# First, you'll need to capture inputs for both Player 1 and Player 2.

# Next, you'll use conditionals to check the two answers and see who wins. This seems pretty
# complicated on the surface but don't overthink it. Here's some help:
# If Player 1 plays Paper, then there are only two conditionals to check against (Rock, Scissors).
# This means for each element, there should be two checks, totalling 6 checks overall. Each check
# should print "Player x wins" with the correct player based on the condition.

# Finally, there should be a check for the same element being played, i.e. if both players play rock
# then an error message should be printed like "Error, you aren't allowed to play the same thing".

# WORK OUT YOUR SOLUTION HERE

import sys
def func():
    print("Player 1, pls choose rock, paper or scissors, type exit if you want to stop")
    player1_input=input()

    print("Player 2, pls choose rock, paper or scissors, type exit if you want to stop")
    player2_input=input()
    return player1_input, player2_input

p1, p2 = func()

scenario1=("Both players had the same, pls retry")
scenario2=("Player 1 won, because he had " + p1 + " and player 2 had " + p2)
scenario3=("Player 2 won, because he had " + p2 + " and player 1 had " + p1)




if p1 == p2:
    print(scenario1)
    py, p2 = func()
elif p1 == "rock" and p2 == "scissors":
    print(scenario2)
elif p1 == "paper" and p2 =="rock":
    print(scenario2)
elif p1 == "scissors" and p2 =="paper":
    print(scenario2)
elif p2 == "rock" and p1 == "scissors":
    print(scenario3)
elif p2 == "paper" and p1 == "rock":
    print(scenario3)
elif p2 == "scissors" and p1 == "paper":
    print(scenario3)
else:
    sys.exit()
