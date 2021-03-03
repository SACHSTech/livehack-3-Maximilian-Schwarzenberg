"""
-------------------------------------------------------------------------------
Name: problem1.py
Purpose: To determine which group a player is placed in based on their wins.

Author: Schwarzenberg.Maximilian

Created: 03/03/2021
------------------------------------------------------------------------------
"""

 # Define variables
outcome = 0
win = 0
loss = 0

print("******  Tournament Tracker ******")
print("")
print("Enter the wins and losses for your team:")

 # for loop
for i in range(1,7):
  outcome = input("Game outcome (W or L): ")
  if outcome == "W" or outcome == "w":
    win = win + 1
  if outcome == "L"or outcome == "l":
    loss = loss + 1

print("")
print("Win(s): ", win)
print("Loss(es): ", loss)
print("")

 # Win detection for group placement 
if win == 5 or win == 6:
  print("Your team is in Group 1")
elif win == 3 or win == 4:
  print("Your team is in Group 2")
elif win == 1 or win == 2:
  print("Your team is in Group 3")
else:
  print("Your team is eliminated from the tournament")