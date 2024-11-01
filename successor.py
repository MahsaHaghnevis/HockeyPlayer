
def successor(playerPosition , map , obstacles):
    x , y = playerPosition #unpacking the player position
    
    possibleWays = []
    
    #all moves 
    moves = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
    
    for move in moves:
        dx , dy = move
        newX , newY = x + dx , y + dy
       