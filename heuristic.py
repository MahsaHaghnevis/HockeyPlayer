import math 

def heuristic(playerPosition, balls , goals):
   nearestBallDistance = math.inf
   for ball in balls:
       distance = math.sqrt((playerPosition[0] - ball[0])**2 + (playerPosition[1] - ball[1])**2)
       nearestBallDistance = min(nearestBallDistance , distance)
   
   
   nearestGoalDistance = math.inf
    