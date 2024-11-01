
def successor(playerPosition , map , obstacles):
    x , y = playerPosition #unpacking the player position
    
    possibleWays = []
    
    #all moves 
    moves = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
    
    