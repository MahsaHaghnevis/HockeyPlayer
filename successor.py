
def successor(playerPosition , map , obstacles):
    x , y = playerPosition #unpacking the player position
    
    possibleWays = []
    
    #all moves 
    moves = {'U' : (x-1 , y) ,
             'D':(x+1 , y) , 
             'L':(x , y-1) , 
             'R':(x , y+1)}
    
    for move in moves:
        dx , dy = move
        newX , newY = x + dx , y + dy
            
        if newX < 0 or newY < 0 or newX >= len(map) or newY >= len(map[0]):
            continue
        
        if (newX , newY) in obstacles:
            continue
        possibleWays.append((newX , newY))
        
    return possibleWays
