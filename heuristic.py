import math 

def heuristic(playerPosition, balls , goals):
   nearestBallDistance = math.inf
   for ball in balls:
       distance = math.sqrt((playerPosition[0] - ball[0])**2 + (playerPosition[1] - ball[1])**2)
       nearestBallDistance = min(nearestBallDistance , distance)
   
   
   nearestGoalDistance = math.inf
   
   ballGoalDistance = 0 
   for ball in balls :
       for goal in goals :
              distance = math.sqrt((ball[0] - goal[0])**2 + (ball[1] - goal[1])**2)
              ballGoalDistance = min(ballGoalDistance , distance)
    