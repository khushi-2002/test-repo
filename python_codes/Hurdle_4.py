def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    turn_left()
    move()
    
    while not right_is_clear() and not at_goal():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear() and not at_goal():
        move()
        
    turn_left()
    
while not at_goal():
    
    while wall_in_front():
        jump()
        
    while front_is_clear() and not at_goal():
        move()