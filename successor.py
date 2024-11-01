
def successor(playerPosition , map , obstacles):
    x , y = playerPosition #unpacking the player position
    
    possibleWays = []
    
    #all moves 
    moves = {'U' : (x-1 , y) ,
             'D':(x+1 , y) , 
             'L':(x , y-1) , 
             'R':(x , y+1)}
    
    for dir , (newX , newY) in moves.items():
      
        if newX < 0 or newY < 0 or newX >= len(map) or newY >= len(map[0]):
            continue
        
        if (newX , newY) in obstacles and map[newX][newY][1] == 'X':
            continue
        
        possibleWays.append((dir , (newX , newY)))
        
    return possibleWays
