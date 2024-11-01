def mapPars(input):
    rows , cols = map(int , input[0].split())
    
    gameMap = []
    playerPosition = None
    balls = []
    goals = []
    obstacles = []
    
    availableCells = ['B' , 'G' , 'P' , 'X']
    
    for i in range (1 , rows+1):
        row =  input[i].split(' ')
        gameRow = []
        
        for j in range(cols):
            cell = row[j]
            
            if cell[-1] in availableCells:
                cost = int( cell[:-1])
                obj = cell[-1]
                
            
            gameRow.append((obj , cost))
            
            
            #finding positions needed
            if obj == 'P': #player position
                playerPosition = (i-1 , j) 
                
            elif obj == 'B': #a ball posiition
                balls.append((i-1 , j))
                
            elif obj == 'G': #goal position
                goals.append((i-1 , j))
                
            elif obj == 'X': #obstacle position
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