#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() != True:
    if is_facing_north() == True:
        if right_is_clear() == True:
            turn_right()
            move()
            turn_right()
        else: 
            move()
    else:
        if front_is_clear() == True:
            move()
        elif wall_in_front() == True:
            turn_left()
        