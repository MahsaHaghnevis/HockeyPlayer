def mapPars(input):
    rows , cols = map(int , input[0].split())
    
    gameMap = []
    playerPosition = None
    balls = []
    goals = []
    obstacles = []
    
    
    for i in range (1 , rows+1):
        row =  input[i].split()
        gameRow = []
        
        for j in range(cols):
            cell = row[j]
            
            gameRow.append(cell)
            
            
            #finding positions needed
            if cell == 'P': #player position
                playerPosition = (i-1 , j) 
        