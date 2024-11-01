def mapPars(input):
    rows , cols = map(int , input[0].split())
    
    gameMap = []
    playerPosition = None
    balls = []
    goals = []
    obstacles = []
    
    
    for i in range (1 , rows+1):
        row =  input[i].split(' ')
        gameRow = []
        
        for j in range(cols):
            cell = row[j]
            
            gameRow.append(cell)
            
            
            #finding positions needed
            if cell == 'P': #player position
                playerPosition = (i-1 , j) 
                
            elif cell == 'B': #a ball posiition
                balls.append((i-1 , j))
                
            elif cell == 'G': #goal position
                goals.append((i-1 , j))
                
            elif cell == 'X': #obstacle position
                obstacles.append((i-1 , j))
                
        gameMap.append(gameRow)
        
    return {
        "gameMap" : gameMap,
        "playerPosition" : playerPosition,
        "balls" : balls,
        "goals" : goals,
        "obstacles" : obstacles
        
    }
        
input_lines = [
    "6 10",
    "1P 1 1 1 0 X 1 1 1 1",
    "0 X 1 1 0 0 0 1 0 X",
    "0 0 1 2B 2 2 2B 1 0 0",
    "1 1 0 X X 2 2 1 1G 1",
    "1 1 0 0 0 2 1 1 1 1",
    "1 1 1 1 1 1G 1 1 1 1"
]
print(mapPars(input_lines))