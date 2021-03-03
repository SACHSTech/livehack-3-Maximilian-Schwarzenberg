"""
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: To enter the distance driven for each day until the total distance driven surpasses 100km and see the average and number of days it took. 

Author: Schwarzenberg.Maximilian

Created: 03/03/2021
------------------------------------------------------------------------------
"""

print("***** Welcome to the DoorDash Distance Tracker ****** ")
print("")

day = 0
distance = 0
travelled = 0

print("** Travel Log **")
while travelled < 100:
  distance = float(input("Enter the distance travelled for the day: "))
  travelled = travelled + distance
  day = day + 1

average = travelled // day

average = round(average,0)

print("")
print("** Summary **")
print("It took", str(day) ,"days to surpass 100km driven.")
print("The average distance driven per day is", str(average))