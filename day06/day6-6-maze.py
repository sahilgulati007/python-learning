#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#not done by self
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while at_goal() != True:
    if right_is_clear()== True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()